import sqlite3
import csv
import logging

from src.config import DB_PATH, CSV_PATH, LOG_PATH


logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def init_database():
    # Check if CSV exists
    if not CSV_PATH.exists():
        logging.error(f"CSV file not found: {CSV_PATH}")
        print(f"Error: CSV file not found at {CSV_PATH}")
        return

    try:
        with open(CSV_PATH, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

        if not rows:
            raise ValueError("CSV file is empty")

        columns = rows[0].keys()

        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            cursor.execute("DROP TABLE IF EXISTS employees")
            cursor.execute(
                f"CREATE TABLE employees ({', '.join(col + ' TEXT' for col in columns)})"
            )

            placeholders = ", ".join(["?"] * len(columns))
            insert_query = (
                f"INSERT INTO employees ({', '.join(columns)}) VALUES ({placeholders})"
            )

            for row in rows:
                cursor.execute(insert_query, tuple(row.values()))

        logging.info("Database initialized successfully")
        print("Database created successfully.")

    except Exception:
        logging.exception("Failed to initialize database")
        print("Database initialization failed. Check logs for details.")


if __name__ == "__main__":
    init_database()
