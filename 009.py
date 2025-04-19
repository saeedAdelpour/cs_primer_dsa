import math


def fn1(n):
    # O(1)
    return n * n


def f2(n):
    return math.sqrt(n)


def bin_sqrt(n):
    """
    O(log(n))

    binary search between 1 and n - 1
    for a k such that k * k <= n
    and (k + 1) * (k + 1) > n
    """


def lin_sqrt(n):
    """
    O(sqrt(n))

    for k in 1 to n - 1
    if k * k <= n
    and (k + 1) * (k + 1) > n
    return k
    """


def factorial_rec1(n):
    """
    O(n)

    for i in 1 to n
    multiply i

    space complexity: O(n)
    """
    if n == 1:
        return 1

    return n * factorial_rec1(n - 1)


def factorial_rec2(n, acc):
    """
    O(n)

    for i in 1 to n
    multiply i

    space complexity: O(n)
    """

    if n == 1:
        return acc

    return factorial_rec2(n - 1, acc * n)


"""
tail call optimization: convert any recursive function to iterative
this optimization causes the space complexity to be O(1)
"""


def iter_fac(n):
    """
    O(n)

    for i in 1 to n
    multiply i

    space complexity: O(1)
    """

    acc = 1
    for i in range(1, n + 1):
        acc *= i

    return acc


def fib(n):
    """
    O(2^n)
    space complexity: O(n)

    when cache results:
    O(n)
    space complexity: O(n)
    """
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


def iter_fib(n):
    """
    O(n)
    space complexity: O(1)
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
