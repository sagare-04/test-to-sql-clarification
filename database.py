
import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv

# Load database configuration
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env", override=True)


def get_connection():
    """Create a connection to MySQL."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )


def execute_select(query, params=None):
    """Execute a SELECT query and return column names and rows."""
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(query, params or ())

        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()

        return columns, rows

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


def display_results(columns, rows):
    """Display query results in the terminal."""
    if not rows:
        print("No records found.")
        return

    print(" | ".join(columns))
    print("-" * 50)

    for row in rows:
        print(" | ".join(str(value) for value in row))


if __name__ == "__main__":
    try:
        print("\nTEST 1: Show all customers\n")

        columns, rows = execute_select(
            "SELECT id, customer_name, city FROM customers"
        )
        display_results(columns, rows)

        print("\nTEST 2: Show customers from Berlin\n")

        columns, rows = execute_select(
            "SELECT customer_name, city FROM customers WHERE city = %s",
            ("Munich",),
        )
        display_results(columns, rows)

    except mysql.connector.Error as error:
        print("Database error:", error)