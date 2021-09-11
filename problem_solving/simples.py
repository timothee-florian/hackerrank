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
