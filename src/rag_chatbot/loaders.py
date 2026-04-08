import json
from pathlib import Path
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader


def load_pdf(path: str):
    loader = PyPDFLoader(path)
    return loader.load()


def load_languages_json(path: str):
    path_obj = Path(path)
    data = json.loads(path_obj.read_text(encoding="utf-8"))

    text = (
        f"{data['section']}\n\n"
        f"Õpitavad keeled: {', '.join(data['languages'])}.\n\n"
        f"Õppimise kestus: {data['learning_time_note']}"
    )

    return [
        Document(
            page_content=text,
            metadata={
                "source": "Keelekataloog",
                "doc_type": "language_catalog",
                "section": data["section"]
            }
        )
    ]