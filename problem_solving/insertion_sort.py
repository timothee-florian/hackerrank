# https://www.hackerrank.com/challenges/insertionsort1/problem
# sorting
def insertionSort1(n, arr):
    # Write your code here
    i = len(arr)-1
    last = arr[-1]
    while i >= 0:
        if i > 0  and arr[i-1] > last:
            arr[i] = arr[i-1]
            print(' '.join([str(x) for x in arr]))
        else:
            arr[i] = last
            print(' '.join([str(x) for x in arr]))
            break
        i -= 1