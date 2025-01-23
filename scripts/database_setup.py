import os
import sqlite3

import pandas as pd

db_path = os.path.join("database", "invoices.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute(
    """
               CREATE TABLE invoices (
    id INTEGER PRIMARY KEY,
    invoice_id INTEGER,
    client_name TEXT,
    issue_date TEXT,
    due_date TEXT,
    amount REAL,
    payment_date TEXT
)
"""
)

csv_path = os.path.join("data", "invoices.csv")
df = pd.read_csv(csv_path)

df.to_sql("invoices", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print(f"Database created and data inserted at {db_path}")
