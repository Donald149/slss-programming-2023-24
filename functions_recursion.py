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


def fib(n: int) -> int:
    """Calculate and return the nth
    Fibonacci number.
    
    Params:
        n - the nth number

    Returns:
        the nth Fibonaccci number
    """
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)
    
print(fib(10))