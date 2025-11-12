#!/usr/bin/env python3
# https://projecteuler.net/problem=27

# For quadratic formula: n² + a*n + b
# b must be prime because for n = 0, the result is b
# n < b -> b² + ab + b = b (b + a + 1)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return False
    return True


def quadratic_primes(max_value):
    max_primes = 0
    product = 0

    prime_b_values = [b for b in range(2, max_value + 1) if is_prime(b)]

    for a in range(-max_value + 1, max_value):
        for b in prime_b_values:
            n = 0
            while n < b and is_prime(n**2 + a*n + b):
                n += 1
            if n > max_primes:
                max_primes = n
                product = a * b

    return product

if __name__ == '__main__':
    print(quadratic_primes(1000))

