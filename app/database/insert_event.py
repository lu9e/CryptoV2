from datetime import datetime, timezone
from app.database.connection import SessionLocal
from app.database.models import MarketEventDB
from app.intelligence.event_analyzer import analyze_event
from app.schemas.events import RawMarketEvent



# Creating a raw market event containing the original information before any kind of analysis or processing has been done. 
raw_event = RawMarketEvent(
    timestamp = datetime.now(timezone.utc),
    source="SEC",
    source_type="REGULATORY_RELEASE",
    text="The SEC announces new regulatory guidance concerning cryptocurrency markets.",
)

analyzed_event = analyze_event(raw_event)

# Creating the database session that allows the application to interact with the PostgreSQL database.
db = SessionLocal()

# MarketEventDB is the SQLAlchemy model that represents the market_events table and calling it will create 
# a new Python object that represents a new row in the market_events table.
event = MarketEventDB(
    timestamp = analyzed_event.timestamp.replace(tzinfo=None),
    source=analyzed_event.source,
    source_type=analyzed_event.source_type,
    text=analyzed_event.text,
    category=analyzed_event.category,
    sentiment=analyzed_event.sentiment.value,
    severity=analyzed_event.severity.value,
    confidence=analyzed_event.confidence,
    affected_assets=analyzed_event.affected_assets,
)


# Attempt to register the new event using the db.add(event) as well as committing it to PostgreSQL and printing a success message
# with an exception catch to handle any potential errors during the insertion with the protocol being to roll back the database session and display an error message.
try:
    db.add(event)
    db.commit()
    print("Event inserted successfully.")

except Exception as error:
    db.rollback()
    print(f"Failed to insert event: {error}")
    raise

finally:
    db.close()



