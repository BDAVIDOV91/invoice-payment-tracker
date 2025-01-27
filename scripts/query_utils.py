import os
import sqlite3

import pandas as pd


def get_connection():
    db_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "database",
        "invoices.db",
    )
    print(f"Database path: {db_path}")  # Debugging line
    return sqlite3.connect(db_path)


def get_all_invoices():
    conn = get_connection()
    query = "SELECT * FROM invoices"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def get_overdue_invoices():
    conn = get_connection()
    query = """
    SELECT * FROM invoices
    WHERE payment_date IS NULL AND due_date < DATE('now')
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def get_paid_invoices():
    conn = get_connection()
    query = """
    SELECT * FROM invoices
    WHERE payment_date IS NOT NULL
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
