"""Example"""


def calculate_factorial(n):
    """Calculate the factorial of a given integer.

    This function takes an integer 'n' as input and calculates its factorial.

    Parameters:
        n (int): The integer for which the factorial needs to be calculated.

    Returns:
        int: The factorial of the input integer 'n'.

    """
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i  # This is a long line of code that calculates the factorial of 'n'.
    return factorial
