from sqlalchemy import Column, String, Integer, DateTime, Numeric, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from helpers.config import Config as config
# from helpers.exception import DatabaseException

dburl = f"postgresql+psycopg2://{config.db_user}:{config.db_pass}@{config.db_host}:{config.db_port}/{config.db_name}"

engine = create_engine(dburl)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class DataNasabah(Base):
    __tablename__ = "data_nasabah"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    nik = Column(String, unique=True, index=True)
    no_hp = Column(String, unique=True, index=True)
    no_rekening = Column(String, unique=True, index=True)
    saldo = Column(Numeric, default=0)  # Field saldo dengan default 0
    created_at = Column(DateTime, default=datetime.utcnow)  # Field created_at
    modified_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Field modified_at

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

