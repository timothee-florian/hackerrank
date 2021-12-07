# https://www.hackerrank.com/challenges/missing-numbers/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
from collections import Counter
def missingNumbers(arr, brr):
    # Write your code here
    c_arr = Counter(arr)
    c_brr = Counter(brr)
    for k, v in c_brr.items():
        c_brr[k] = c_brr[k] - c_arr.get(k, 0)
    out = []
    for k, v in c_brr.items():
        out += [k] * v
    return sorted(list(set(out)))
