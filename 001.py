#!/usr/bin/env python3
# https://projecteuler.net/problem=1

def multiples_sum(k, n):
    m = (n - 1) // k
    return k * m * (m + 1) // 2

if __name__ == '__main__':
    n = 1000 
    result = multiples_sum(3, n) + multiples_sum(5, n) - multiples_sum(15, n)
    print(result)

