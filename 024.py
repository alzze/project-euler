#!/usr/bin/env python3
# https://projecteuler.net/problem=24

import math 

def lexicographic_permutation(n):
    x = [i for i in range(10)]
    result = []

    while x:
        fact = math.factorial(len(x) - 1)
        index = n // fact
        n = n % fact
        result.append(str(x.pop(index)))
    return "".join(result)
        

if __name__ == '__main__':
    print(lexicographic_permutation(999999))
