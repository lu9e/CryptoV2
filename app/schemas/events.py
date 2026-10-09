from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from enum import Enum




#Establishing allowed values for event sentiment, severity, and source type.
#Implement enums to help prevent inconsistent values from entering the pipeline. 
class Sentiment(str, Enum):
    BULLISH = "BULLISH"
    BEARISH  = "BEARISH"
    NEUTRAL = "NEUTRAL"


class Severity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class SourceType(str, Enum):
    NEWS = "NEWS"
    PRESIDENTIAL_SPEECH = "PRESIDENTIAL_SPEECH"
    GOVERNMENT_RELEASE = "GOVERNMENT_RELEASE"
    REGULATORY_RELEASE = "REGULATORY_RELEASE"
    EXCHANGE_ANNOUNCEMENT = "EXCHANGE_ANNOUNCEMENT"
    PROTOCOL_ANNOUNCEMENT = "PROTOCOL_ANNOUNCEMENT"
    COMPANY_ANNOUNCEMENT = "COMPANY_ANNOUNCEMENT"
    
#RawMarketEvent will represent incoming news/announcements before any kind of analysis.
#Pydantic validates the time stamp as well as the source, source_type, and event text.
class RawMarketEvent(BaseModel):
    timestamp: datetime
    source: str
    source_type: SourceType
    text: str


#EventAnalysis will store the intelligence generated from a raw event.
#Confidence range is also established to value between 0 and 1.
class EventAnalysis(BaseModel):
    category: str
    sentiment: Sentiment
    severity: Severity
    confidence: float = Field(ge=0.0, le=1.0)
    affected_assets: List[str]


#MarketEvent combines the the original incoming event data with analysis results.
#Inheriting from RawMarketEvent avoids repeating the incoming event fields.
class MarketEvent(RawMarketEvent):
    category: str
    sentiment: Sentiment
    severity: Severity
    confidence: float = Field(ge=0.0, le=1.0)
    affected_assets: List[str]











