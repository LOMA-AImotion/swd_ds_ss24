"""
Some utility functions for numbers
"""

from numbers import Number

def add_numbers(a: Number, b: Number) -> Number:
    """ This function takes two numbers as inputs and returns their sum

    Args:
        a (Number): first summand
        b (Number): second summand

    Returns:
        Number:  the sum of the two inputs
    """
    result = a + b 
    return result

if __name__ == "__main__":
    print(add_numbers(10, 15))