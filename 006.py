#!/usr/bin/env python3
# https://projecteuler.net/problem=6

def difference(n):
    # ⅙ n (n + 1) (2n + 1) - n (1 + n) / 2
    return (n * (1 + n) / 2 ) **2 - 1/6 * n * (n +1) * (2*n +1)

if __name__ == '__main__':
    print(difference(100))
