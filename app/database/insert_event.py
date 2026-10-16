from datetime import datetime, timezone
from app.database.connection import SessionLocal
from app.database.models import MarketEventDB




# Creating the database session that allows the application to interact with the PostgreSQL database.
db = SessionLocal()

# MarketEventDB is the SQLAlchemy model that represents the market_events table and calling it will create 
# a new Python object that represents a new row in the market_events table.
event = MarketEventDB(
    timestamp = datetime.now(timezone.utc).replace(tzinfo=None),
    source="SEC",
    source_type="REGULATORY_RELEASE",
    text="The SEC announces new regulatory guidance concerning cryptocurrency markets.",
    category="REGULATION",
    sentiment="BEARISH",
    severity="HIGH",
    confidence=0.91,
    affected_assets=["BTC", "ETH", "SOL"],
)


# Register and commit the new event with the SQlAlchemy session, which will prepare it to be inserted into the market_events table.
db.add(event)
db.commit()
db.close()

