from rag_chatbot.config import PDF_FILE
from rag_chatbot.loaders import load_pdf
from rag_chatbot.cleaners import clean_text
from rag_chatbot.chunkers import chunk_faq_documents


def main():
    docs = load_pdf(str(PDF_FILE))

    for doc in docs:
        doc.page_content = clean_text(doc.page_content)
        doc.metadata["source"] = "Tallinna Keeltekooli KKK"

    chunks = chunk_faq_documents(docs)

    print(f"Chunke kokku: {len(chunks)}")
    print("=" * 50)

    for i, chunk in enumerate(chunks[:5], start=1):
        print(f"\nCHUNK {i}")
        print("QUESTION:", chunk.metadata.get("question"))
        print("SECTION:", chunk.metadata.get("section"))
        print("TEXT:")
        print(chunk.page_content[:500])
        print("-" * 50)


if __name__ == "__main__":
    main()