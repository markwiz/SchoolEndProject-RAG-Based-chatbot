from rag_chatbot.chains import answer_question


def main():
    print("Tallinna Keeltekooli Qdrant RAG demo. Kirjuta 'exit', et lõpetada.\n")

    while True:
        question = input("Küsimus: ").strip()

        if question.lower() in {"exit", "quit"}:
            print("Tšau.")
            break

        response, docs = answer_question(question)

        print("\nVastus:")
        print(response.content)

        print("\nAllikad:")
        for i, doc in enumerate(docs, start=1):
            print(f"{i}. {doc.metadata.get('section')} | {doc.metadata.get('question')}")

        print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()