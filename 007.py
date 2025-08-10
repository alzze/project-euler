#!/usr/bin/env python3
# https://projecteuler.net/problem=7

def is_prime(n, primes):
    for p in primes :
        if p * p > n:
            break
        if n % p == 0:
            return 0
    return 1

def prime(n):
    primes = []
    x = 2
    while len(primes) < n:
        if is_prime(x,primes):
            primes.append(x)
        x += 1
    return primes[-1]

if __name__ == '__main__':
    print(prime(10001))
