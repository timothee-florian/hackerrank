# https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
def maxSubsetSum(arr):
    max_values = [max(arr[0], 0)]
    max_values += [max(arr[:2] + [0])]
    for v in arr[2:]:
        max_values+= [max(v+max_values[-2], max_values[-1])]
    return max_values[-1]