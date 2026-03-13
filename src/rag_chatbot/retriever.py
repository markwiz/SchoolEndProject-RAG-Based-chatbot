from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

from rag_chatbot.config import QDRANT_PATH, COLLECTION_NAME, EMBEDDING_MODEL


def get_vectorstore() -> QdrantVectorStore:
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    vectorstore = QdrantVectorStore.from_existing_collection(
        embedding=embeddings,
        path=str(QDRANT_PATH),
        collection_name=COLLECTION_NAME,
    )
    return vectorstore


def get_retriever():
    vectorstore = get_vectorstore()
    return vectorstore.as_retriever(search_kwargs={"k": 4})