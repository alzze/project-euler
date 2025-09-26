#!/usr/bin/env python3
# https://projecteuler.net/problem=25
''' 
https://www.youtube.com/watch?v=3vbHTi6sID0
    phi = (1 + math.sqrt(5)) / 2
    math.ceil((d - 1 + math.log10(math.sqrt(5))) / math.log10(phi))
'''

import math

def fibonacci_digits(d):
    a, b = 1, 1   
    n = 2         
    while len(str(b)) < d:  
        a, b = b, a + b    
        n += 1
    return n
    
if __name__ == '__main__':
    print(fibonacci_digits(1000))
