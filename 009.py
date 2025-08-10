#!/usr/bin/env python3
# https://projecteuler.net/problem=9

def pythagorean_triplet(x):
    a, b, c = 0, 0, 0
    m = 1
    while True: 
        for n in range(m):
            a = m * m - n * n 
            b = 2 * m * n
            c = m * m + n * n
            if (a + b + c == 1000):
                return a * b * c
        m += 1
            
if __name__ == '__main__':
    print(pythagorean_triplet(1000))
