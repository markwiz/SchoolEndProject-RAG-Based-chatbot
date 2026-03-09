from rag_chatbot.config import PDF_FILE
from rag_chatbot.loaders import load_pdf
from rag_chatbot.cleaners import clean_text


def main():
    docs = load_pdf(str(PDF_FILE))

    first_doc = docs[0]
    cleaned = clean_text(first_doc.page_content)

    print("ENNE:")
    print(first_doc.page_content[:700])
    print("\n" + "=" * 50 + "\n")
    print("PÄRAST:")
    print(cleaned[:700])


if __name__ == "__main__":
    main()