#!/usr/bin/env python3
# https://projecteuler.net/problem=14

def largest_collatz(n):
    mem = {1:1}
    number = max_length = 1

    for x in range(2,n):
        value = x
        length = 0

        while value not in mem:
            if not value % 2 :
                value //= 2
                length += 1
            else:
                value = (3 *  value + 1) // 2
                length += 2
        mem[x] = length + mem[value]

        if mem[x] > max_length:
            max_length = mem[x]
            number = x
    return number

        

if __name__ == '__main__':
    print(largest_collatz(1000000))
