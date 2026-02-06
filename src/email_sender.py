import smtplib
import logging
from email.message import EmailMessage

from src.config import (
    SMTP_HOST,
    SMTP_PORT,
    SMTP_USERNAME,
    SMTP_PASSWORD,
)


class SmtpEmailSender:
    def send(self, to_email, subject, body):
        if not SMTP_USERNAME or not SMTP_PASSWORD:
            raise RuntimeError("SMTP credentials are not configured")

        msg = EmailMessage()
        msg["From"] = SMTP_USERNAME
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(body)

        try:
            with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USERNAME, SMTP_PASSWORD)
                server.send_message(msg)

            logging.info(f"Email sent successfully to {to_email}")

        except Exception:
            logging.exception(f"Failed to send email to {to_email}")
            raise
