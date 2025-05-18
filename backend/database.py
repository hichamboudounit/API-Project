from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://admin:admin@db:5432/sampledb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
