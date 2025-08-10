#!/usr/bin/env python3
# https://projecteuler.net/problem=16

def power_digit_sum(n):
    return sum(int(digit) for digit in str(2 ** n))

if __name__ == '__main__':
    print(power_digit_sum(1000))
