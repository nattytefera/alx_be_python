# robust_division_calculator.py
def safe_divide(numerator, denominator):
    """
    Safely performs division, handling errors for zero division and non-numeric inputs.

    Parameters:
        numerator (str): The numerator as a string input.
        denominator (str): The denominator as a string input.

    Returns:
        str: Result of the division or an appropriate error message.
    """
    try:
        num = float(numerator)
        denom = float(denominator)

        if denom == 0:
            return "Error: Cannot divide by zero."

        return f"The result of the division is {num / denom}"

    except ValueError:
        return "Error: Please enter numeric values only."
