# https://www.hackerrank.com/challenges/grid-challenge/problem
# suposedly greedy
def gridChallenge(grid):

    grid2 = [sorted(s) for s in grid]
    gridT = {}

    for i in range(len(grid2[0])):
        gridT[i] = []
        for j in range(len(grid2)):          
            gridT[i].append(grid2[j][i])

    sorted_grid = {i:sorted(s) for i, s in gridT.items()}
    if gridT == sorted_grid:
        return 'YES'
    return 'NO'