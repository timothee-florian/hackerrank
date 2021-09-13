# https://www.hackerrank.com/challenges/non-divisible-subset/problem
def nonDivisibleSubset(k, s):
    # Write your code here
    n = 0
    s_modulo = [v%k for v in s]
    count_modulo = {}
    for v in s_modulo:
        count_modulo[v] = count_modulo.get(v, 0) + 1
    for i in range(k // 2+1):
        
        if i == 0 or i == k / 2:
            n += min(1, count_modulo.get(i, 0))
        else:
            n += max(count_modulo.get(k-i, 0), count_modulo.get(i, 0))
        # print(i, n)
    # print(count_modulo)
    return n