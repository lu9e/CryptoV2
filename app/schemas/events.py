from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from enum import Enum


# MarketEvent will act as the blueprint; so whenever a announcement or news 
# enter is entering the pipeline Pydantic will make sure the program has the following
# 4 types of raw data

#If there is a missing or wrong data type there will be a proper validation error
#compared to crashing the application

#Establishing the data schema by inheriting from the BaseModel of Pydantic
#date to track how recent the event is 
#where the event is coming from ->White House OR Exchange Announcement
#where the source is coming from ->President OR Government OR News outlet/agency
# #the headline -> the raw context/text that will be analyzed

#may add more attributes for better accuracy which should be coming from the LLM

#Old class 
# class MarketEvent(BaseModel):
#     timestamp: datetime
#     source: str 
#     source_type: str
#     text: str

#     category: str
#     sentiment: Sentiment
#     severity: Severity
#     confidence: float = Field(ge=0.0, le=1.0)

#     #Since we know now what we are dealing with based on the collected event
#     #we have to determine which currency this event actually is targeting 
#     #BTC, ETH, SOL, XRP, XMR
#     affected_assets: List[str]



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
    

# RawMarketEvent represents event data before intelligence analysis. This raw data can later be passed to the LLM layer.
class RawMarketEvent(BaseModel):
    timestamp: datetime
    source: str
    source_type: SourceType
    text: str

class MarketEvent(RawMarketEvent):
    category: str
    sentiment: Sentiment
    severity: Severity
    confidence: float = Field(ge=0.0, le=1.0)
    affected_assets: List[str]











