#!/usr/bin/env python3
# https://projecteuler.net/problem=12

def divisible_triangular(n):
    divisors, x, t = 0, 0, 0
    while divisors <= n:
        i = 1
        x += 1
        t += x 
        divisors = 0 
        while i * i <= t:
            if t % i == 0:
                divisors += 2
            i += 1
    return t 

if __name__ == '__main__':
    print(divisible_triangular(500))
