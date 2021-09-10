# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def minimumSwaps(arr):
    arr2 ={}
    for i, v in enumerate(arr):
        arr2[i] = v - 1
    c= 0
    i = 0
    while i < len(arr):
        if arr2[i] != i:
            temp = arr2[i]
            arr2[i] = arr2[arr2[i]]
            arr2[temp] = temp
            c += 1
            i -= 1
        i += 1
    return c 