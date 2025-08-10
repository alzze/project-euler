#!/usr/bin/env python3
#https://projecteuler.net/problem=5

def evenly_divisible(n):
    x = 1
    for i in range(2, n):
        x = lcm(x,i)
    return x

def lcm(a, b):
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    return abs(a * b) // x

if __name__ == '__main__':
    print(evenly_divisible(20))
