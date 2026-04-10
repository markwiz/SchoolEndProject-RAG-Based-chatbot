import hashlib
import re

from rag_chatbot.db import SessionLocal
from rag_chatbot.models import ResponseCache


def normalize_question(question: str) -> str:
    q = question.strip().lower()
    q = re.sub(r"\s+", " ", q)
    return q


def question_hash(question: str) -> str:
    return hashlib.sha256(question.encode("utf-8")).hexdigest()


def get_cached_answer(question: str):
    normalized = normalize_question(question)
    qh = question_hash(normalized)

    with SessionLocal() as db:
        row = db.query(ResponseCache).filter(ResponseCache.question_hash == qh).first()
        return row


def save_cached_answer(question: str, intent: str, answer_text: str, sources: list):
    normalized = normalize_question(question)
    qh = question_hash(normalized)

    with SessionLocal() as db:
        existing = db.query(ResponseCache).filter(ResponseCache.question_hash == qh).first()
        if existing:
            return

        row = ResponseCache(
            question_hash=qh,
            question_normalized=normalized,
            intent=intent,
            answer_text=answer_text,
            sources_json=sources,
        )
        db.add(row)
        db.commit()