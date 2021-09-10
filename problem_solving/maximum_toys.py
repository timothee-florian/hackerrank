# https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
def maximumToys(prices, k):
    sum_spent = 0
    n_toy = 0
    for price in sorted(prices):
        sum_spent += price
        if sum_spent> k:
            break
        n_toy += 1
    return n_toy