# Functions and Recursion
# Author: Donald
# 6 December 2023


def factorial(num: int) -> int:
    """Returns the result of the number's 
    factorial using recursion
    
    Params:
        num - number we're calculating

    Returns:
        result
    """
    if num == 0 or num == 1:
        return 1
    elif num > 1:
        return num * factorial(num - 1)


print(factorial(5))
