#!/usr/bin/env python3
# https://projecteuler.net/problem=22

def names_score(file):
    with open("names.txt") as f:
        names = f.read().replace('"', '').split(',')
    names.sort()
    return  sum((i+1) * sum(ord(c) - ord('A') + 1 for c in name) for i, name in enumerate(names))

if __name__ == '__main__':
    print(names_score('names.txt'))
