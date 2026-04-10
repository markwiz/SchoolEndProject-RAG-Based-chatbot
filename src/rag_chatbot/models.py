from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from datetime import datetime

from rag_chatbot.db import Base


class ResponseCache(Base):
    __tablename__ = "response_cache"

    id = Column(Integer, primary_key=True)
    question_hash = Column(String(128), unique=True, nullable=False)
    question_normalized = Column(Text, nullable=False)
    intent = Column(String(50), nullable=False)
    answer_text = Column(Text, nullable=False)
    sources_json = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class UnansweredQuestion(Base):
    __tablename__ = "unanswered_questions"

    id = Column(Integer, primary_key=True)
    user_question = Column(Text, nullable=False)
    normalized_question = Column(Text, nullable=False)
    label = Column(String(50), nullable=True)
    reason = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)