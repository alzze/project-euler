#!/usr/bin/env python3
# https://projecteuler.net/problem=26

def reciprocal_cycle(limit):
    max_len, best_d = 0, 0

    for d in range(1, limit):
        temp = d
        while temp % 2 == 0: temp //= 2
        while temp % 5 == 0: temp //= 5
        if temp == 1: continue

        seen, x, i = {}, 1, 0
        while True:
            if x in seen:
                length = i - seen[x]
                break
            seen[x], x, i = i, (x * 10) % d, i + 1

        if length > max_len:
            max_len, best_d = length, d

    return best_d


if __name__ == "__main__":
    print(reciprocal_cycle(1000))

