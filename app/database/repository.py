#Repository would be for database operations and responsible for interacting with stored data.

#The plan is to create functions to handle CRUD operations (Create, Read, Update, Delete) for the database.
#Saving analyzed market events to PostgreSQL database.
#Retrieving previously stored events.
#Looking up events by IDs if needed.


from app.database.models import MarketEventDB
from app.schemas.events import MarketEvent 
from sqlalchemy.orm import Session


def save_event(db: Session, event: MarketEvent) -> MarketEventDB:
    db_event = MarketEventDB()
    db_event.timestamp = event.timestamp.replace(tzinfo=None)
    db_event.source = event.source
    db_event.source_type = event.source_type
    db_event.text = event.text
    db_event.category = event.category
    db_event.sentiment = event.sentiment.value
    db_event.severity = event.severity.value
    db_event.confidence = event.confidence
    db_event.affected_assets = event.affected_assets
    db.add(db_event)
    db.flush()
    return db_event





    





