from fastapi import FastAPI
from pydantic import BaseModel

from rag_chatbot.chains import answer_question

app = FastAPI()


class AskRequest(BaseModel):
    question: str


@app.post("/ask")
def ask(req: AskRequest):
    response, docs = answer_question(req.question)

    return {
        "answer": response.content,
        "sources": [
            {
                "section": doc.metadata.get("section"),
                "question": doc.metadata.get("question"),
                "source": doc.metadata.get("source"),
            }
            for doc in docs
        ],
    }