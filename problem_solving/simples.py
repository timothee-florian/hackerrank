# https://www.hackerrank.com/challenges/ctci-big-o/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous
def primality(n):
    if n == 1:
        return 'Not prime'
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 'Not prime'
    return 'Prime'

# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
def makeAnagram(a, b):
    # Can only delete letters
    # Anagram <=> letters count
    letter_count_a = {}
    letter_count_b = {}
    for letter in a:
        letter_count_a[letter] = letter_count_a.get(letter, 0) + 1
    for letter in b:
        letter_count_b[letter] = letter_count_b.get(letter, 0) + 1
    n_deletions = 0
    letters = set(a+b)
    for letter in letters:
        n_deletions += abs(letter_count_a.get(letter,0)-letter_count_b.get(letter,0))
    return n_deletions

# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
def alternatingCharacters(s):
    n_deletion = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            n_deletion += 1
    return n_deletion

# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
def isValid(s):
    count_letters = {}
    has_only_unique = True
    for letter in s:
        count_letters[letter] = count_letters.get(letter, 0) + 1
    number_occurence = {}
    ks = set()
    for k, v in count_letters.items():
        number_occurence[v] = number_occurence.get(v, 0)+1
        ks.add(v)
    print(count_letters)
    print(number_occurence)
    print(ks)
    if len(ks) == 1:
        return 'YES' #all appears same num of time
    elif len(ks) == 2:
        if max(ks) == min(ks) +1  and number_occurence[max(ks)] == 1:
            return 'YES'
        elif number_occurence[min(ks)] == 1:
            return 'YES'
# https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues
def isBalanced(s):
    stack = []
    for l in s:
        if l in '{[(':
            stack.append(l)
        elif l == ']':
            if len(stack) >0 and stack[-1] == '[':
                stack.pop(-1)
            else:
                return 'NO'
        elif l == '}':
            if len(stack) >0 and stack[-1] == '{':
                stack.pop(-1)
            else:
                return 'NO'    
        elif l == ')':
            if len(stack) >0 and stack[-1] == '(':
                stack.pop(-1)
            else:
                return 'NO' 
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'