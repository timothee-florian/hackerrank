# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
def organizingContainers(container):
    # Write your code here
    n_types = [0] * len(container)
    n_container = []
    for c in container:
        n_container += [sum(c)]
        for i in range(len(c)):
            n_types[i] = n_types[i] + c[i]
    if sorted(n_container) == sorted(n_types):
        return 'Possible'
    return 'Impossible'
