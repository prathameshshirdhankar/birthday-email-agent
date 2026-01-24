import sqlite3
import pandas as pd

CSV_PATH = r"D:\AI Agent\test_employees.csv"
DB_PATH = r"D:\AI Agent\employees.db"

# Load CSV
df = pd.read_csv(CSV_PATH)

# Create SQLite DB
conn = sqlite3.connect(DB_PATH)

df.to_sql("employees", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully: employees.db")
