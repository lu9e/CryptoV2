from datetime import datetime
import pytest
from app.schemas.events import RawMarketEvent, EventAnalysis
from app.intelligence.event_analyzer import generate_analysis, analyze_event
from pydantic import ValidationError

#Check the regulatory keyword are classified under REGULATION.
def test_regulatory_event_category():
    raw_event = RawMarketEvent(
        timestamp = datetime.now(),
        source="SEC",
        source_type = "REGULATORY_RELEASE",
        text = "New regulatory guidance concerning cryptocurrency markets."
    )
    analysis = generate_analysis(raw_event)
    assert analysis.category == "REGULATION"


#Check that events without regulatory keywords fall under OTHER.
def test_protocol_event_category():
    raw_event = RawMarketEvent(
        timestamp = datetime.now(),
        source="Ethereum Foundation",
        source_type="PROTOCOL_ANNOUNCEMENT",
        text="Ethereum announces a major network upgrade."
    )
    analysis = generate_analysis(raw_event)
    assert analysis.category == "OTHER"


#Making sure that the original event information is preserved after analysis
def test_raw_event_data_is_preserved():
    timestamp = datetime(2026, 10, 5, 12, 0, 0)
    raw_event = RawMarketEvent(
        timestamp=timestamp,
        source="Ethereum Foundation",
        source_type="PROTOCOL_ANNOUNCEMENT",
        text="Ethereum announces a major network upgrade."
    )

    event = analyze_event(raw_event)
    assert event.timestamp == timestamp
    assert event.source == raw_event.source
    assert event.source_type == raw_event.source_type
    assert event.text == raw_event.text


#Confidence must stay between 0 and 1.
#Values outside that given range should throw an error.
def test_invalid_confidence_is_rejected():
    with pytest.raises(ValidationError):
        EventAnalysis(
            category="REGULATION",
            sentiment="BEARISH",
            severity="HIGH",
            confidence=1.5,
            affected_assets=["BTC", "ETH"]
        )