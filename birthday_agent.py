import sqlite3
from datetime import datetime
import logging

# ================= CONFIG =================
# All configurable values live here.
# This makes the script easier to adjust without digging into logic.

DB_PATH = r"D:\AI Agent\employees.db"   # Path to the employee SQLite database
LOG_PATH = r"D:\AI Agent\agent.log"     # Log file for agent activity

COMPANY_NAME = "TestOrg"                # Used in email content and signature

# =========================================


def setup_logging():
    """
    Configure application-wide logging.
    Logs are written to a file so runs can be audited later.
    """
    logging.basicConfig(
        filename=LOG_PATH,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


def get_todays_birthdays():
    """
    Retrieve employees whose birthday falls on today's date.
    Only month and day are compared; the year is intentionally ignored.
    """
    today = datetime.today().strftime("%m-%d")

    # Open database connection
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Select employees with matching month/day
    query = """
        SELECT name, email
        FROM employees
        WHERE strftime('%m-%d', date_of_birth) = ?
    """

    cursor.execute(query, (today,))
    rows = cursor.fetchall()

    # Close connection to avoid resource leaks
    conn.close()

    return rows


def send_individual_email(name, email):
    """
    Simulate sending a professional birthday email.
    This function only prints output and logs activity.
    """
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

    # Log email activity for traceability
    logging.info(f"Birthday email sent to {name} <{email}>")

    # Simulated email output
    print("----- EMAIL SENT (SIMULATED) -----")
    print(f"To      : {email}")
    print(f"Subject : {subject}")
    print(body)
    print("---------------------------------\n")


def run_agent():
    """
    Entry point for the daily birthday agent.
    Runs once, checks for birthdays, and sends emails if needed.
    """
    setup_logging()
    logging.info("Daily birthday agent run started")

    rows = get_todays_birthdays()

    # Exit early if there are no birthdays today
    if not rows:
        logging.info("No birthdays today")
        print("No birthdays today.")
        return

    logging.info(f"{len(rows)} birthday(s) found today")
    print(f"Found {len(rows)} birthday(s) today.\n")

    # Send emails one by one
    for name, email in rows:
        send_individual_email(name, email)

    logging.info("Daily birthday agent run completed successfully")


if __name__ == "__main__":
    # Script entry point
    run_agent()
