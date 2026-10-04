from datetime import datetime
from app.schemas.events import RawMarketEvent
from app.intelligence.event_analyzer import analyze_event


#focused on creating a simple raw event to represent fake data as incoming events before the analysis.
# raw_event = RawMarketEvent(
#     timestamp=datetime.now(),
#     source="SEC",
#     source_type="REGULATORY_RELEASE",
#     text="New regulatory guidance concerning cryptocurrency markets."
# )


raw_event = RawMarketEvent(
    timestamp=datetime.now(),
    source="Ethereum Foundation",
    source_type="PROTOCOL_ANNOUNCEMENT",
    text="Ethereum announces a major network upgrade."
)

#Displaying the event before the analysis for better transparency of the before and after output.
print("RAW EVENT:")
print(raw_event)


#Were than passing the raw_event into the analyze_event to test the functionality of the pipeline.
#analyze_event should preserve the raw event data while taking the hard coded analysis 
event = analyze_event(raw_event)

print("\nANALYZED EVENT:")
print(event)









