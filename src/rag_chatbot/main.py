from rag_chatbot.config import PDF_FILE
from rag_chatbot.loaders import load_pdf


def main():
    docs = load_pdf(str(PDF_FILE))

    print(f"Laetud dokumente: {len(docs)}")
    print("-" * 50)
    print(docs[0].page_content[:1000])
    print("-" * 50)
    print(docs[0].metadata)


if __name__ == "__main__":
    main()