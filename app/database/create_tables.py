# At this point in the application a connection was established to the PostgreSQL
# database using SQLAlchemy's create_engine function.

#The next step would be to create the necessary tables in the database based on the defined models.

from app.database.connection import engine
from app.database.models import Base 


# The SQLAlchemy uses the engine to connect to the cryptov2 PostgreSQL database.
# It will read the table definitions registered with the Base class.

#  Base.metadata.create_all(bind=engine) creates the market_evenets table if it didn't already exist in the database.
Base.metadata.create_all(bind=engine)
print("Database tables were created successfully with no errors found. ")



