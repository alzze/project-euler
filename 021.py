#!/usr/bin/env python3
# https://projecteuler.net/problem=21


def d(n):
    if n == 1:
        return 0
    result = 1
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            result += i
            if i != n // i: 
                result += n // i
    return result

def amicable_sum(n):
    result = 0
    for i in range(2, n):
       if d(i) != i and d(d(i)) == i :
           result += i
    return result

if __name__ == '__main__':
    print(amicable_sum(10000))
