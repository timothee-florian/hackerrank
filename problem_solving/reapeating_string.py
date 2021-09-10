# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
def repeatedString(s, n):
    # Write your code here
    if n <= len(s):
        return s[:n].count('a')
    n_repetition = n // len(s)
    residu = n % len(s)
    n_a = n_repetition * s.count('a') + s[:residu].count('a')
    return n_a