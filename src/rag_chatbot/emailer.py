import os
import smtplib
from email.message import EmailMessage


def send_handoff_email(user_question: str, answer_text: str, label: str):
    smtp_host = os.getenv("SMTP_HOST", "smtp.zone.eu")
    smtp_port = int(os.getenv("SMTP_PORT", "465"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    handoff_to = os.getenv("HANDOFF_EMAIL")

    msg = EmailMessage()
    msg["Subject"] = f"Chatbot fallback: {label}"
    msg["From"] = smtp_user
    msg["To"] = handoff_to

    msg.set_content(
        f"Kasutaja küsimus:\n{user_question}\n\n"
        f"Boti vastus:\n{answer_text}\n\n"
        f"Label:\n{label}\n"
    )

    with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
        server.login(smtp_user, smtp_password)
        server.send_message(msg)