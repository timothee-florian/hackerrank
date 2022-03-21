# https://www.hackerrank.com/challenges/icecream-parlor/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=60-day-campaign
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    arr2 = sorted(arr)
    arr3 = sorted(range(len(arr)), key=lambda k: arr[k])
    i, j = 0, len(arr)-1
    while i <= j:
        if arr2[i] + arr2[j] < m:
            i += 1
        elif arr2[i] + arr2[j] > m:
            j -= 1
        else:            
            return sorted([arr3[i]+1, arr3[j]+1])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
