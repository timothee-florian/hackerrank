# https://www.hackerrank.com/challenges/pairs/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def pairs(k, arr):
    # Write your code here
    c_n= Counter(arr) # O(n)
    arr = sorted(list(set(arr)))
    i = 0
    j = 1
    c = 0
    # print(c_n)
    # print(arr)
    while i < len(arr)-1 and j < len(arr):
        # print(i, j)
        if arr[i] < arr[j] - k:
            i += 1
        elif arr[i] > arr[j] - k:
            j += 1
        else:
            c += c_n[arr[i]] * c_n[arr[j]]
            j += 1
    return c