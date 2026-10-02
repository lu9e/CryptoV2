from datetime import datetime
#from app.schemas.events import MarketEvent
from app.schemas.events import RawMarketEvent, MarketEvent

#hard coded data for a test run using the schema
#also making sure if the LLM outputs the wrong data type the application wil be able catch it

#simple test will be instead of float being placed for confidence the LLM enters a str
#by mistake

# event = MarketEvent(
#     timestamp = datetime.now(),
#     source="SEC",
#     source_type = "REGULATORY_RELEASE",
#     text="New regulatory guidance concerning cryptocurrency markets.",
#     category="REGULATION",
#     sentiment="BEARISH",
#     severity="HIGH",
#     confidence="HIGH ",
#     affected_assets=["BTC","ETH","SOL"]
# )

#Pydantic's type coercion allows the string float to work aswell
# event = MarketEvent(
#     timestamp = datetime.now(),
#     source="SEC",
#     source_type = "REGULATORY_RELEASE",
#     text="New regulatory guidance concerning cryptocurrency markets.",
#     category="REGULATION",
#     sentiment="BEARISH",
#     severity="HIGH",
#     confidence="0.91",
#     affected_assets=["BTC","ETH","SOL"]
# )


#we want to make sure that the confidence is a valid float that makes sence
#meaning it has to bes less than or equal to 1 with the lower bound being caped at 0
# event = MarketEvent(
#     timestamp = datetime.now(),
#     source="SEC",
#     source_type = "REGULATORY_RELEASE",
#     text="New regulatory guidance concerning cryptocurrency markets.",
#     category="REGULATION",
#     sentiment="BEARISH",
#     severity="HIGH",
#     confidence=500.0,
#     affected_assets=["BTC","ETH","SOL"]
# )

raw_event = RawMarketEvent(
    timestamp=datetime.now(),
    source="SEC",
    source_type="REGULATORY_RELEASE",
    text="New regulatory guidance concerning cryptocurrency markets."
)

print("RAW EVENT:")
print(raw_event)


event = MarketEvent(
    timestamp = datetime.now(),
    source="SEC",
    source_type = "REGULATORY_RELEASE",
    text="New regulatory guidance concerning cryptocurrency markets.",
    category="REGULATION",
    sentiment="BEARISH",
    severity="HIGH",
    confidence=0.91,
    affected_assets=["BTC","ETH","SOL"]
)

print("\nANALYZED EVENT:")
print(event)




