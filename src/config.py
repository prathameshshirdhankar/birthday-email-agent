from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

DB_PATH = DATA_DIR / "employees.db"
CSV_PATH = DATA_DIR / "test_employees.csv"
LOG_PATH = LOG_DIR / "agent.log"

COMPANY_NAME = "TestOrg"

# make sure folders exist so things don't blow up
DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# Email mode: "console" (print only) or "smtp" (real emails)
EMAIL_MODE = "console"   # 🔁 CHANGE TO "smtp" when sending real emails

# SMTP configuration
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

# 🔐 Read credentials from environment variables
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
