from sqlalchemy import create_engine, Column, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# --- Database URL for MySQL (no password) ---
DATABASE_URL = "mysql+pymysql://root@localhost/chatdb"

# --- SQLAlchemy setup ---
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# --- Chat model ---
class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True, index=True)
    user_input = Column(Text, nullable=False)
    bot_reply = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# --- Create tables ---
Base.metadata.create_all(bind=engine)
'''''''''