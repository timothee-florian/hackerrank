# https://www.hackerrank.com/challenges/sherlock-and-gcd/problem
def solve(a):
    # Write your code here
    gcd = a[0] 
    for i in range(len(a)):
        gcd = math.gcd(gcd, a[i])
    if gcd == 1:
        return 'YES'
    else:
        return 'NO'