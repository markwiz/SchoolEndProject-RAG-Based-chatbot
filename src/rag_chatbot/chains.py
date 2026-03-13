from langchain_openai import ChatOpenAI

from rag_chatbot.config import CHAT_MODEL
from rag_chatbot.prompts import QA_PROMPT
from rag_chatbot.retriever import get_retriever


def format_docs(docs) -> str:
    formatted = []
    for doc in docs:
        section = doc.metadata.get("section", "Teadmata sektsioon")
        question = doc.metadata.get("question", "Teadmata küsimus")
        source = doc.metadata.get("source", "Teadmata allikas")

        formatted.append(
            f"[Allikas: {source} | Sektsioon: {section} | Küsimus: {question}]\n{doc.page_content}"
        )

    return "\n\n".join(formatted)


def answer_question(question: str):
    retriever = get_retriever()
    docs = retriever.invoke(question)

    context = format_docs(docs)

    llm = ChatOpenAI(model=CHAT_MODEL, temperature=0)
    chain = QA_PROMPT | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    return response, docs