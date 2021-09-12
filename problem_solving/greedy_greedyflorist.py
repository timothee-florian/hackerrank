# https://www.hackerrank.com/challenges/greedy-florist/problem
def getMinimumCost(k, c):
    c.sort()
    cost = 0
    purchase_person ={}
    for i in range(len(c)-1, -1, -1): # rearange the purchase such as everyone buy expensive and cheap
        key = i % k
        purchase_person[key] = purchase_person.get(key, []) + [c[i]]
        purchase_person[key] = sorted(purchase_person[key])
    for purchase in purchase_person.values():
        # print(purchase)
        for i, price in enumerate(purchase[::-1]):
            cost += (1 + i) * price
    return cost