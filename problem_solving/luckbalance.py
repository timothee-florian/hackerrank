# https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
def luckBalance(k, contests):
    important_contests = []
    unimportant_contests = []
    
    for contest in contests:
        if contest[1]:
            important_contests += [contest[0]]
        else:
            unimportant_contests += [contest[0]]
    luck = sum(unimportant_contests)
    important_contests.sort()
    if k != 0:
        luck += sum(important_contests[-k:])
        luck -= sum(important_contests[:-k])
    else:
        luck -= sum(important_contests)
    return luck