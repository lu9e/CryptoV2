import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker



#Creating the SQLAlchemy connection file.
#Will start by loading the credentials/connection info from the .env file.
load_dotenv()

#Creating a PostgreSQL connnection URL, that will include the passwords/info from the .env file.
database_url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port = int(os.getenv("DB_PORT","5432")),
    database=os.getenv("DB_NAME"),
)

#With the information inputted into the URL connection create SQLAlchemy database connection manager,
#without creating an automaic connection.
engine = create_engine(database_url, pool_pre_ping=True)

#Creating database sessions that would be used to preform operations.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

