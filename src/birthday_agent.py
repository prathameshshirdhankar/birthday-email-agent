import logging

from src.config import LOG_PATH
from src.repository import BirthdayRepository
from src.config import COMPANY_NAME



def setup_logging():
    logging.basicConfig(
        filename = LOG_PATH,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


<<<<<<< HEAD
# Business logic (testable)
def build_birthday_message(name):
    subject = f"Happy Birthday from {COMPANY_NAME}"
=======

# business logic only, keep this clean-ish
def build_birthday_message(userName):
    subject=f"Happy Birthday from {COMPANY_NAME}"
>>>>>>> 1463bb0 (Refactor project structure and improve robustness based on review feedback)

    body = f"""
Dear {userName},

Wishing you a very Happy Birthday!

On behalf of everyone at {COMPANY_NAME}, we hope your special day is filled with happiness, good health, and success.
We truly appreciate your contributions and wish you a wonderful year ahead.

Warm regards,
{COMPANY_NAME}
Human Resources
"""
    return subject , body


<<<<<<< HEAD
# Side effects only (delivery simulation)
def send_individual_email(name, email):
=======

# side effects + printing junk
def send_individual_email(name,email):
>>>>>>> 1463bb0 (Refactor project structure and improve robustness based on review feedback)
    subject, body = build_birthday_message(name)

    logging.info(f"Birthday email sent to {name} <{email}>")

    print("----- EMAIL SENT (SIMULATED) -----")
    print(f"To      : {email}")
    print(f"Subject : {subject}")
    print(body)
    print("---------------------------------\n")



def run_agent():
    try:
        setup_logging()
        logging.info("Daily birthday agent run started")

        repo = BirthdayRepository()
        tempUserList = repo.get_birthdays_for_today()

        if not tempUserList:
            logging.info("No birthdays today")
            print("No birthdays today.")
            return

        logging.info(f"{len(tempUserList)} birthday(s) found today")
        print(f"Found {len(tempUserList)} birthday(s) today.\n")

        for name , email in tempUserList:
            send_individual_email(name,email)

        logging.info("Daily birthday agent run completed successfully")

    except Exception:
        #this is broad, but it's fine for now
        logging.exception("Agent run failed unexpectedly")
        print("Agent failed. Check logs for details.")



if __name__ == "__main__":
    run_agent()
