from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

DB_PATH = DATA_DIR / "employees.db"
CSV_PATH = DATA_DIR / "test_employees.csv"
LOG_PATH = LOG_DIR / "agent.log"

COMPANY_NAME = "TestOrg"


# Ensure required directories exist
DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
