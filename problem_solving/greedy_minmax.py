# https://www.hackerrank.com/challenges/angry-children/problem
def maxMin(k, arr):
    # Write your code here
    arr.sort()
    ar = {}
    min_unfair = float('inf')
    for i, a in enumerate(arr):
        ar[i] = a
    for i in range(len(arr) - k+1):
        min_unfair = min(min_unfair, ar[i+k-1] - ar[i])
    return min_unfair