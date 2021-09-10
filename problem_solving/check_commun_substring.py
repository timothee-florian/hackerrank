# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
def twoStrings(s1, s2):
    # Write your code here
    letters_s1 =set(s1)
    letters_s2 =set(s2)
    if len(letters_s1.intersection(letters_s2))>0:
        return 'YES'
    else:
        return 'NO'