#!/usr/bin/env python3
# https://projecteuler.net/problem=15

from math import factorial

def lattice_paths(n):
    # 2n! / n ! * (2n - n)!
    return factorial(2*n) // (factorial(n) * factorial(n))


if __name__ == '__main__':
    print(lattice_paths(20))
