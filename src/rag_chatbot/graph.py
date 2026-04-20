from typing import TypedDict, Optional

from rag_chatbot.cache import get_cached_answer, save_cached_answer
from rag_chatbot.intent_router import detect_intent
from rag_chatbot.chains import answer_question
from rag_chatbot.confidence import needs_handoff
from rag_chatbot.emailer import send_handoff_email


class GraphState(TypedDict):
    question: str
    intent: Optional[str]
    cached_answer: Optional[str]
    answer: Optional[str]
    needs_handoff: Optional[bool]
    label: Optional[str]


def check_cache(state: GraphState):
    row = get_cached_answer(state["question"])
    if row:
        return {"cached_answer": row.answer_text}
    return {"cached_answer": None}


def classify_intent(state: GraphState):
    return {"intent": detect_intent(state["question"])}


def generate_answer(state: GraphState):
    response, docs = answer_question(state["question"], intent=state["intent"])
    text = response.content

    sources = [
        {
            "section": doc.metadata.get("section"),
            "question": doc.metadata.get("question"),
            "source": doc.metadata.get("source"),
        }
        for doc in docs
    ]

    return {
        "answer": text,
        "needs_handoff": needs_handoff(text, docs),
        "label": state["intent"] or "unknown",
        "sources": sources,
    }


def save_answer(state: GraphState):
    save_cached_answer(
        question=state["question"],
        intent=state["intent"] or "general",
        answer_text=state["answer"] or "",
        sources=state.get("sources", []),
    )
    return {}


def send_email_node(state: GraphState):
    send_handoff_email(
        user_question=state["question"],
        answer_text=state["answer"] or "",
        label=state["label"] or "unknown",
    )
    return {}