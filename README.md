# RAG Chatbot Demo

RAG-põhine chatboti demo, mis kasutab LangChaini, ChromaDB-d ja OpenAI mudeleid, et vastata küsimustele dokumentide põhjal.

Projekt on loodud eesmärgiga teha töötav ja lihtsasti laiendatav esimene versioon, kuhu saab lisada PDF-id, töödelda need chunk'ideks, salvestada vektorandmebaasi ning vastata kasutaja küsimustele ainult teadmistebaasi põhjal.

## Eesmärk

Selle projekti eesmärk on ehitada demo, mis:

- loeb sisse dokumente, näiteks PDF-e
- puhastab ja chunkib teksti loogilisteks osadeks
- loob embeddingud
- salvestab need ChromaDB-sse
- leiab kasutaja küsimusele sobiva konteksti
- genereerib vastuse ainult dokumentidest leitud info põhjal

## Tehnoloogiad

- Python 3.12
- uv
- LangChain
- ChromaDB
- OpenAI API
- FastAPI
- Uvicorn

## Projekti struktuur

```text
rag-chatbot-demo/
├── .gitignore
├── .env
├── .env.example
├── README.md
├── pyproject.toml
├── uv.lock
├── data/
│   ├── raw/
│   └── processed/
├── chroma_db/
├── src/
│   └── rag_chatbot/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       ├── loaders.py
│       ├── cleaners.py
│       ├── chunkers.py
│       ├── ingest.py
│       ├── retriever.py
│       ├── chains.py
│       └── prompts.py
└── tests/