# https://www.hackerrank.com/challenges/two-characters/problem
def check_correctness(s):
    if len(set(s))> 2:
        return False
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return False
    return True

def alternate(s):
    if len(set(s)) == 1: # check limit cases
        return 0
    while True: #cleaning , unecessary
        replaces = set()
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                replaces.add(s[i])
        if len(replaces) == 0:
            break
        for r in replaces:
            s = s.replace(r, '')
    letters = set(s)
    max_length = 0
    for letter1 in letters:
        for letter2 in letters:
            new_s = ''.join([l for l in s if l == letter1 or l ==letter2 ])
            if check_correctness(new_s):
                max_length = max(max_length, len(new_s))
    return max_length