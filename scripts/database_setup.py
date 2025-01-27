import os
import sqlite3

import pandas as pd

# Create a connection to the SQLite database
db_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "database",
    "invoices.db",
)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the invoices table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS invoices (
    invoice_id INTEGER PRIMARY KEY,
    client_name TEXT NOT NULL,
    issue_date TEXT NOT NULL,
    due_date TEXT NOT NULL,
    amount REAL NOT NULL,
    payment_date TEXT
)
"""
)

# Load the CSV data into a DataFrame
csv_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "invoices.csv"
)
df = pd.read_csv(csv_path)

# Rename columns to match the database schema
df.columns = [
    "invoice_id",
    "client_name",
    "issue_date",
    "due_date",
    "amount",
    "payment_date",
]

# Insert the data into the invoices table
df.to_sql("invoices", conn, if_exists="replace", index=False)

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"Database created and data inserted at {db_path}")
