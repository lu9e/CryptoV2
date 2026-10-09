from app.schemas.events import(
    RawMarketEvent,
    MarketEvent,
    EventAnalysis,
    Sentiment,
    Severity,
)


#Separating event analysis from the main processing pipeline. 
#With the current set up being basic keyword ruling and place holder values. With the later 
#plans involving the use of an LLM to generate analysis. 
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

    
#Takes a raw event, and generates its analysis, while combining both into a complete and organized MarketEvent.
#The current pipeline being 
#RawMarketEvent to Rule based analysis to EventAnalysis to a complete MarketEvent
def analyze_event(raw_event: RawMarketEvent) -> MarketEvent:

    analysis = generate_analysis(raw_event)
    
    return MarketEvent(
        #Original information from the raw event as well as the analysis information from EventAnalysis.
        timestamp = raw_event.timestamp,
        source=raw_event.source,
        source_type=raw_event.source_type,
        text = raw_event.text,
        category=analysis.category,
        sentiment=analysis.sentiment,
        severity=analysis.severity,
        confidence=analysis.confidence,
        affected_assets=analysis.affected_assets,
    )
