from app.schemas.events import(
    RawMarketEvent,
    MarketEvent,
    EventAnalysis,
    Sentiment,
    Severity,
)


#Isolate responsibilitY of generating event analysis into its own function.
#This function will later be adjusted to use the LLM compared to the temp rule given logic.
def generate_analysis(raw_event: RawMarketEvent)-> EventAnalysis:
    regulation_keywords = ["regulation", "regulatory"]
    text = raw_event.text.lower()

    if any(keyword in text for keyword in regulation_keywords):
        category = "REGULATION"
    else:
        category = "OTHER"

    return EventAnalysis(
        category=category,
        sentiment=Sentiment.BEARISH,
        severity=Severity.HIGH,
        confidence=0.91,
        affected_assets=["BTC","ETH","SOL"],
    )

    
#This function will take RawMarketEvent generate its analysis, and combine both in to a 
#complete MarketEvent

#at this point the current set up is:
#RawMarketEvent to hard coded analysis to the eventAnalysis and finally to a complete MarketEvent

#later the set up will look like:
#RawMarketEvent to  LLM analysis to EvenAnalysis to a Complete Market Event

def analyze_event(raw_event: RawMarketEvent) -> MarketEvent:

    analysis = generate_analysis(raw_event)
    
    return MarketEvent(
        #original information from the raw event
        timestamp = raw_event.timestamp,
        source=raw_event.source,
        source_type=raw_event.source_type,
        text = raw_event.text,

        #Analysis information from EventAnalysis
        category=analysis.category,
        sentiment=analysis.sentiment,
        severity=analysis.severity,
        confidence=analysis.confidence,
        affected_assets=analysis.affected_assets,
    )
