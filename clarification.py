
def check_clarification(question):
    """
    Check whether a question needs clarification.
    Returns a follow-up question or None.
    """

    question = question.lower().strip()

    # The user wants customers but has not specified a city.
    if question in [
        "show customers",
        "list customers",
        "show customers from",
        "show customers in",
        "list customers from",
        "list customers in",
    ]:
        return "Which city would you like to see customers from?"

    # No clarification needed for the supported questions.
    return None


if __name__ == "__main__":
    test_questions = [
        "Show customers",
        "Show customers from",
        "Show customers in Berlin",
        "Show all customers",
    ]

    for question in test_questions:
        clarification = check_clarification(question)

        print(f"\nQuestion: {question}")

        if clarification:
            print(f"Clarification: {clarification}")
        else:
            print("Clarification: Not needed")