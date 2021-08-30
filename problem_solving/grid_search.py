# https://www.hackerrank.com/challenges/the-grid-search/problem
def gridSearch(G, P):
    # Write your code here
    for i in range(len(G) - len(P)+1):
        positions = []
        not_here = False
        for j in range(len(P)):
            positions_j = set([ind.start() for ind in re.finditer(f'(?={P[j]})', G[i+j])])
            if len(positions_j) == 0:
                not_here =True
                # break
            positions.append(positions_j)
        if not not_here:
            s_position = positions[0]
            for s in positions:
                s_position = s_position.intersection(s)
            if len(s_position) > 0:
                return 'YES'
    return 'NO'
