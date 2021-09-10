# https://www.hackerrank.com/challenges/candies/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
# This simple algo pass all test but does not use dynamic programing
def candies(n, arr):
    if arr[1]<arr[0]:
        candies1 = [2]
    else:
        candies1 = [1]
    for i in range(1,n):
        if arr[i]> arr[i-1]:
            candies1 += [candies1[-1] +1]
        else:
            candies1 += [1]
    if arr[-2]<arr[-1]:
        candies2 = [2]
    else:
        candies2 = [1]
    for i in range(n-2,-1, -1):
        if arr[i]> arr[i+1]:
            candies2 += [candies2[-1] +1]
        else:
            candies2 += [1]
    candies2 = candies2[::-1]   
    candies_final = [] 
    for i in range(n):
        candies_final += [max(candies1[i], candies2[i])] 
    return sum(candies_final)