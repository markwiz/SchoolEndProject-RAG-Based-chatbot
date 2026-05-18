from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import HTMLResponse

from rag_chatbot.chains import answer_question

app = FastAPI()


class AskRequest(BaseModel):
    question: str

@app.get("/")
def root():
    return {"status": "API running"}

@app.get("/chat", response_class=HTMLResponse)
def chat_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>RAG CHATBOT</title>
    </head>
    <body>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #f4f6f9;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .chat-container {
            width: 600px;
            background: white;
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        h1 {
            text-align: center;
            margin-bottom: 25px;
            color: #333;
        }

        .input-row {
            display: flex;
            gap: 10px;
        }

        input {
            flex: 1;
            padding: 14px;
            border: 1px solid #ccc;
            border-radius: 10px;
            font-size: 16px;
        }

        button {
            padding: 14px 22px;
            border: none;
            border-radius: 10px;
            background: #4f46e5;
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: 0.2s;
        }

        button:hover {
            background: #4338ca;
        }

        .answer-box {
            margin-top: 25px;
            background: #f9fafb;
            border-radius: 12px;
            padding: 20px;
            min-height: 120px;
            color: #222;
            line-height: 1.6;
            border: 1px solid #e5e7eb;
        }

        .loading {
            color: gray;
            font-style: italic;
        }
    </style>

    <div class="chat-container">
        <h1>RAG Chatbot</h1>

        <div class="input-row">
            <input
                type="text"
                id="question"
                placeholder="Ask something..."
            >

            <button onclick="askQuestion()">
                Send
            </button>
        </div>

        <div class="answer-box">
            <div id="answer">
                Your answer will appear here...
            </div>
        </div>
    </div>

    <script>
        async function askQuestion() {
            const question = document.getElementById("question").value;

            document.getElementById("answer").innerHTML =
                "<span class='loading'>Thinking...</span>";

            const response = await fetch("/ask", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    question: question
                })
            });

            const data = await response.json();

            document.getElementById("answer").innerText =
                data.answer;
        }
    </script>
</body>
</html>
    """

@app.post("/ask")
def ask(req: AskRequest):
    response, docs = answer_question(req.question)

    return {
        "answer": response.content,
        "sources": [
            {
                "section": doc.metadata.get("section"),
                "question": doc.metadata.get("question"),
                "source": doc.metadata.get("source"),
            }
            for doc in docs
        ],
    }