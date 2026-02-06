import sqlite3
from datetime import datetime
import logging

from src.config import DB_PATH


class BirthdayRepository:
    def get_birthdays_for_today(self):
        today = datetime.today().strftime("%m-%d")

        query = """
            SELECT name, email
            FROM employees
            WHERE strftime('%m-%d', date_of_birth) = ?
        """

        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(query, (today,))
                return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
            return []
