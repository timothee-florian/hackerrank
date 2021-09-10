# https://www.hackerrank.com/challenges/larrys-array/problem
# look at https://en.wikipedia.org/wiki/15_puzzle 
def larrysArray(A):
    # the 15 puzzle rule tell that if the number of permutation is dd the sorting is not possible
    n_inversion = 0
    for i in range(len(A) - 1):
        for j in range(i+1 , len(A)):
            if A[i] > A[j]:
                n_inversion +=1
    if n_inversion%2==0:
        return 'YES'
    else:
        return 'NO'