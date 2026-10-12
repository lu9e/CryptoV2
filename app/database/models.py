#With this project I want to be able to store these market event permanently.
#With the current pipeline being 
#RawMarketEvent -> EventAnalysis -> MarketEvent
#to
#RawMarketEvent -> EventAnalysis -> MarketEvent -> PostgreSQL

#This file will be dedicated to defining SQLAlchemy models used for database tables.
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, DateTime, Float, Text, JSON
from datetime import datetime


#Base class that our database models will inherit from.
#SQLAlchemy uses it to register models and their table definitions.
class Base(DeclarativeBase):
    pass



#At this point in the application MarketEvent in app/schemas/events.py is a Pydantic model
#used to validate analyzed events.
#
#MarketEventDB here is a SQLAlchemy model used to store those events permanently in PostgreSQL.


#This represents the PostgreSQL market_events table.
#Which inherits from Base to register the model with SQLAlchemy.
class MarketEventDB(Base):
    #Telling SQLAlchemy that the model corresponds to a PostgreSQL table
    __tablename__ = "market_events"

    id: Mapped[int] = mapped_column(primary_key=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime, nullable=False)










