# https://www.hackerrank.com/challenges/py-if-else/problem
import math
import os
import random
import re
import sys

def is_weird(n):
    if n % 2:
        print('Weird')
    elif n <= 5:
        print('Not Weird')
    elif n <= 20:
        print('Weird')
    else:
        print('Not Weird')

if __name__ == '__main__':
    n = int(raw_input().strip())
    is_weird(n)