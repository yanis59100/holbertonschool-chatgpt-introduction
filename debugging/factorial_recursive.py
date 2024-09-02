#!/usr/bin/python3
import sys

def factorial(n):
    """
    Compute the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): The non-negative integer for which to compute the factorial.

    Returns:
    int: The factorial of the given integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
