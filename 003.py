#!/usr/bin/env python3
#https://projecteuler.net/problem=3

def largest_prime_factor(n):
    f= 2
    while f**2 <= n:
        if n % f == 0:
            n //= f
        else:
            f+= 1 if f == 2 else 2
    return n if n > 1 else f

if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
    
