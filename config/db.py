import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL", ""), future=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False)

meta = MetaData()

# conn = engine.connect()
