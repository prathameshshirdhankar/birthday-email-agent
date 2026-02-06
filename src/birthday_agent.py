import logging

from src.config import LOG_PATH
from src.repository import BirthdayRepository
from src.config import COMPANY_NAME

#Email (SMTP)
from src.config import EMAIL_MODE
from src.email_sender import SmtpEmailSender


def setup_logging():
    logging.basicConfig(
        filename=LOG_PATH,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


# ✅ Pure business logic (testable)
def build_birthday_message(name):
    subject = f"Happy Birthday from {COMPANY_NAME}"

    body = f"""
Dear {name},

Wishing you a very Happy Birthday!

On behalf of everyone at {COMPANY_NAME}, we hope your special day is filled with happiness, good health, and success.
We truly appreciate your contributions and wish you a wonderful year ahead.

Warm regards,
{COMPANY_NAME}
Human Resources
"""
    return subject, body


# ✅ Delivery logic (console OR SMTP)
def send_individual_email(name, email):
    subject, body = build_birthday_message(name)

    if EMAIL_MODE == "smtp":
        sender = SmtpEmailSender()
        sender.send(email, subject, body)
        print(f"Email sent to {email}")
    else:
        print("----- EMAIL SENT (SIMULATED) -----")
        print(f"To      : {email}")
        print(f"Subject : {subject}")
        print(body)
        print("---------------------------------\n")

    logging.info(f"Birthday email processed for {name} <{email}>")


def run_agent():
    try:
        setup_logging()
        logging.info("Daily birthday agent run started")

        repository = BirthdayRepository()
        rows = repository.get_birthdays_for_today()

        if not rows:
            logging.info("No birthdays today")
            print("No birthdays today.")
            return

        logging.info(f"{len(rows)} birthday(s) found today")
        print(f"Found {len(rows)} birthday(s) today.\n")

        for name, email in rows:
            send_individual_email(name, email)

        logging.info("Daily birthday agent run completed successfully")

    except Exception:
        logging.exception("Agent run failed unexpectedly")
        print("Agent failed. Check logs for details.")


if __name__ == "__main__":
    run_agent()
