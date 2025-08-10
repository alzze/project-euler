#!/usr/bin/env python3
#https://projecteuler.net/problem=2

def even_fibonacci(n):
    # E(n) = 4 x E(n-1) + E(n-2) 
    a, b = 2, 8
    s = 2
    while b <= n:
        s += b
        a, b = b, 4 * b+a
    return s

if __name__ == '__main__': 
    print(even_fibonacci(4000000))
