from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from rag_chatbot.config import (
    PDF_FILE,
    CHROMA_DIR,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
)
from rag_chatbot.loaders import load_pdf
from rag_chatbot.cleaners import clean_text
from rag_chatbot.chunkers import chunk_faq_documents


def ingest():
    docs = load_pdf(str(PDF_FILE))

    for doc in docs:
        doc.page_content = clean_text(doc.page_content)
        doc.metadata["source"] = "Tallinna Keeltekooli KKK"

    chunks = chunk_faq_documents(docs)

    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(CHROMA_DIR),
    )

    vectorstore.add_documents(chunks)

    print(f"Ingest valmis. Salvestati {len(chunks)} chunki.")


if __name__ == "main":
    ingest()