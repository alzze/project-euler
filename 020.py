#!/usr/bin/env python3
# https://projecteuler.net/problem=20

from math import factorial

def factorial_digits_sum(n):
    result = 0
    f = factorial(n)
    while f > 0:
        result += f % 10
        f //= 10

    return result

if __name__ == '__main__':
    print(factorial_digits_sum(100))
