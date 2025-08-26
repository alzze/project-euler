#!/usr/bin/env python3
# https://projecteuler.net/problem=19

def count_sundays(n):
    start, end = (n - 1) * 100 + 1, n * 100
    result = 0
    for y in range(start, end + 1):
        for m in range(1, 13):
            year, month = y, m
            if month < 3:
                month += 12
                year -= 1
            q = 1
            K = year % 100
            J = year // 100
            h = (q + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
            if h == 1:
                result += 1
    return result

if __name__ == '__main__':
    print(count_sundays(20))
