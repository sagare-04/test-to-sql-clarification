
from database import execute_select
from clarification import check_clarification

def generate_sql(question):
    """Convert supported English questions into SQL."""

    question = question.lower().strip()

    if question in [
        "show all customers",
        "list all customers",
        "display all customers",
    ]:
        return (
            "SELECT id, customer_name, city FROM customers",
            (),
        )

    if question in [
        "show customers from berlin",
        "show customers in berlin",
        "list customers in berlin",
    ]:
        return (
            "SELECT customer_name, city FROM customers WHERE city = %s",
            ("Berlin",),
        )

    if question in [
        "show customers from munich",
        "show customers in munich",
        "list customers in munich",
    ]:
        return (
            "SELECT customer_name, city FROM customers WHERE city = %s",
            ("Munich",),
        )

    return None, None



def main():
    question = input("Ask a question about your customers: ").strip()

    # Step 1: Check whether clarification is needed.
    clarification = check_clarification(question)

    if clarification:
        print(f"\nClarification: {clarification}")
        answer = input("Your answer: ").strip()

        if not answer:
            print("No answer provided. Please try again.")
            return

        # Build a complete question from the original request and answer.
        question = f"Show customers in {answer}"

    # Step 2: Generate SQL from the complete question.
    query, params = generate_sql(question)

    if query is None:
        print("I don't understand this question yet.")
        print("Please try asking about all customers or a city.")
        return

    # Step 3: Execute SQL and display the results.
    try:
        columns, rows = execute_select(query, params)

        print("\nResults:")

        if not rows:
            print("No records found.")
            return

        print(" | ".join(columns))
        print("-" * 40)

        for row in rows:
            print(" | ".join(str(value) for value in row))

    except Exception as error:
        print(f"Something went wrong: {error}")


if __name__ == "__main__":
    main()