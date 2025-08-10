#!/usr/bin/env python3
# https://projecteuler.net/problem=17

UNITS = [
    "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen"
]
TENS = [
    "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
]

def letter_counts(n):
    def num_to_words(x):
        if x == 1000:
            return "onethousand"
        if x >= 100:
            hundreds = UNITS[x // 100] + "hundred"
            remainder = x % 100
            if remainder:
                return f"{hundreds}and{num_to_words(remainder)}"
            return hundreds
        if x >= 20:
            tens = TENS[x // 10]
            units = UNITS[x % 10]
            return f"{tens}{units}"
        return UNITS[x]
    return sum(len(num_to_words(i)) for i in range(1, n + 1))

if __name__ == '__main__':
    print(letter_counts(1000))
