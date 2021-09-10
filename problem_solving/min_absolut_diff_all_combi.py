# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    min_diff = float('inf')
    for i in range(1, n):
        min_diff = min(min_diff, abs(arr[i-1]-arr[i]))
    return min_diff