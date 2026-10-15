
import re


def validate_sql(query):
    """
    Allow only a single read-only SELECT query.
    Returns (is_valid, message).
    """

    if not query or not query.strip():
        return False, "Query cannot be empty."

    query = query.strip()

    # Remove one optional trailing semicolon.
    if query.endswith(";"):
        query = query[:-1].rstrip()

    # Reject multiple SQL statements.
    if ";" in query:
        return False, "Multiple SQL statements are not allowed."

    # Only SELECT queries are allowed.
    if not re.match(r"^SELECT\b", query, re.IGNORECASE):
        return False, "Only SELECT queries are allowed."

    # Reject common SQL write or administrative operations.
    forbidden = re.compile(
        r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|CREATE|TRUNCATE|"
        r"REPLACE|GRANT|REVOKE|CALL|EXEC|EXECUTE|"
        r"INTO\s+OUTFILE|INTO\s+DUMPFILE|LOAD_FILE)\b",
        re.IGNORECASE,
    )

    if forbidden.search(query):
        return False, "Query contains a forbidden operation."

    return True, "Query is valid."


if __name__ == "__main__":
    test_queries = [
        "SELECT * FROM customers",
        "SELECT customer_name FROM customers WHERE city = 'Berlin';",
        "DELETE FROM customers",
        "DROP TABLE customers",
        "SELECT * FROM customers; DELETE FROM customers",
        "",
    ]

    for query in test_queries:
        is_valid, message = validate_sql(query)
        print(f"\nQuery: {query!r}")
        print(f"Valid: {is_valid}")
        print(f"Message: {message}")