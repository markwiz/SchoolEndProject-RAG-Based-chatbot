from langchain_core.documents import Document


def is_question(line: str) -> bool:
    return line.strip().endswith("?")


def is_possible_heading(line: str) -> bool:
    line = line.strip()
    if not line:
        return False
    if line.endswith("?"):
        return False
    if len(line) > 80:
        return False
    return line[0].isupper()


def chunk_faq_documents(docs):
    chunks = []

    for doc in docs:
        lines = [line.strip() for line in doc.page_content.splitlines() if line.strip()]

        current_section = None
        current_question = None
        current_answer = []

        for line in lines:
            if is_possible_heading(line):
                if current_question and current_answer:
                    chunks.append(
                        Document(
                            page_content=f"{current_question}\n\n{' '.join(current_answer)}",
                            metadata={
                                **doc.metadata,
                                "doc_type": "faq",
                                "section": current_section,
                                "question": current_question,
                            },
                        )
                    )
                    current_question = None
                    current_answer = []

                current_section = line
                continue

            if is_question(line):
                if current_question and current_answer:
                    chunks.append(
                        Document(
                            page_content=f"{current_question}\n\n{' '.join(current_answer)}",
                            metadata={
                                **doc.metadata,
                                "doc_type": "faq",
                                "section": current_section,
                                "question": current_question,
                            },
                        )
                    )

                current_question = line
                current_answer = []
            else:
                if current_question:
                    current_answer.append(line)

        if current_question and current_answer:
            chunks.append(
                Document(
                    page_content=f"{current_question}\n\n{' '.join(current_answer)}",
                    metadata={
                        **doc.metadata,
                        "doc_type": "faq",
                        "section": current_section,
                        "question": current_question,
                    },
                )
            )

    return chunks