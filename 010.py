#!/usr/bin/env python3
# https://projecteuler.net/problem=10

def summation_primes(n):
    primes = [True] * n
    primes[0] = primes[1] = False 

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False

    return sum(i for i, is_prime in enumerate(primes) if is_prime)

if __name__ == '__main__':
    print(summation_primes(2000000))
