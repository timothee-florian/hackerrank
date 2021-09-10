# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
def checkMagazine(magazine, note):
    # Write your code here
    magazine_words = {}
    for word in magazine:
        magazine_words[word] = magazine_words.get(word, 0) + 1
    works = True
    for word in note:
        n = magazine_words.get(word, 0)
        if n == 0:
            print('No')
            works = False
            break
        magazine_words[word] = n-1
    if works:
        print('Yes')  