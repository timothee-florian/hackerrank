# https://www.hackerrank.com/challenges/beautiful-triplets/problem
# implementation
def beautifulTriplets(d, arr):
    values = set(arr)
    c = 0
    for a in arr:
        if a + d in values and a + 2 * d in values:
            c += 1
    return c