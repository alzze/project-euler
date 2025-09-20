#!/usr/bin/env python3
# https://projecteuler.net/problem=23

def is_abundant(n):
    d = 1
    for i in range(2, int(n ** 0.5)+ 1):
        if d > n:
            return True
        if n % i == 0:
            d += i
            if i != n // i:
                d += n // i
    return d > n

def non_abundant_sum(max):
    abundant_numbers = [i for i in range(12, max + 1) if is_abundant(i)] 
    result = [False] * (max + 1)
    for i in abundant_numbers:
        for j in abundant_numbers:
            if i + j <= max:
                result[i + j] = True
            else:
                break
    return sum(i for i in range(1, max) if not result[i])


if __name__ == '__main__':
    print(non_abundant_sum(28123))
