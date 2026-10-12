
def generate_sql(question):
    """
    Convert a simple English question into a SQL query.
    Returns the SQL query and its parameters.
    """

    question = question.lower().strip()

    # Rule 1: Show all customers
    if question in [
        "show all customers",
        "list all customers",
        "display all customers",
    ]:
        return (
            "SELECT id, customer_name, city FROM customers",
            ()
        )

    # Rule 2: Find customers in a particular city
    if question in [
        "show customers from berlin",
        "show customers in berlin",
        "list customers in berlin",
    ]:
        return (
            "SELECT customer_name, city FROM customers WHERE city = %s",
            ("Berlin",)
        )

    if question in [
        "show customers from munich",
        "show customers in munich",
        "list customers in munich",
    ]:
        return (
            "SELECT customer_name, city FROM customers WHERE city = %s",
            ("Munich",)
        )

    # No matching rule found
    return None, None


if __name__ == "__main__":
    test_questions = [
        "Show all customers",
        "Show customers in Berlin",
        "Show customers in Munich",
        "Show me the most popular product",
    ]

    for question in test_questions:
        query, params = generate_sql(question)

        print(f"\nQuestion: {question}")
        print(f"SQL: {query}")
        print(f"Parameters: {params}")