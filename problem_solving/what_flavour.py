# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
# search index use dict to be more time efficient
# Single solution guarantied
def whatFlavors(cost, money):
    cost_dict = {}
    for i, c in enumerate(cost):
        if c in cost_dict:
            cost_dict[c] = [[i] + cost_dict[c][0], cost_dict[c][1] +1]
        else:
            cost_dict[c] = [[i], 1]
    
    for i, c in enumerate(cost):
        temp_money = money -c
        cost_dict[c][1] = cost_dict[c][1] - 1
        if temp_money in cost_dict and cost_dict[temp_money][1]> 0:
            print(i+1, cost_dict[temp_money][0][0]+1)
            break #bit more optimal