# https://www.hackerrank.com/challenges/extra-long-factorials/problem

def extraLongFactorials(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    print(output)

# Strangely easy for medium level dificulty
