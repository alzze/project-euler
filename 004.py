#!/usr/bin/env python3
#https://projecteuler.net/problem=4

def largest_palindrome(n):
    x = 0
    for i in range(10 ** n, 10 ** (n-1), -1):
        for j in range (i, 10 ** (n-1), -1):
            if i * j <= x:
                break
            if str(i * j) == str(i * j)[::-1]:
                x = i * j
    return x

if __name__ == '__main__':
    print(largest_palindrome(3))


