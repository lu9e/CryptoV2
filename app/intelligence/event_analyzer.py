from app.schemas.events import(
    RawMarketEvent,
    MarketEvent,
    Sentiment,
    Severity,
)


#This will handle raw events data with the purpose of returning the analyzed MarketEvent.
#The info that will be used for analysis is currently hard coded for the purpose of having a working and testable pipeline
#and easier LLM integration; 


#Current setup: RawMarketEvent -> rule-based/hard-coded analysis -> MarketEvent
#Later setup: RawMarketEvent -> LLM analysis -> MarketEvent
def analyze_event(raw_event: RawMarketEvent) -> MarketEvent:

    regulation_keywords = ["regulation", "regulatory"]
    

    text = raw_event.text.lower()

    #Temp rule based classification used to identify regulatory events.
    #any() checks whether at least one keyword appears in the event text.
    if any(keyword in text for keyword in regulation_keywords):
        category = "REGULATION"
    else: 
        category = "OTHER"

    
    return MarketEvent(
        #original information from the raw event
        timestamp = raw_event.timestamp,
        source=raw_event.source,
        source_type=raw_event.source_type,
        text = raw_event.text,

        
        category=category,
        sentiment=Sentiment.BEARISH,
        severity=Severity.HIGH,
        confidence=0.91,
        affected_assets=["BTC","ETH","SOL"],
    )
