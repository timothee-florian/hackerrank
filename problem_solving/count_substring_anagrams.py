# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# Simply get all possible substring and count how may time they appear, them just get the number of combiantions for the number
def sherlockAndAnagrams(s):

    n_sub = {}
    for i in range(len(s)):
        sb = ''
        for j in range(i, len(s)):
            sb = ''.join(sorted(sb + s[j]))
            n_sub[sb] = n_sub.get(sb, 0) + 1
  
    n = 0
    for k, v in n_sub.items():
        n += (v*(v-1))//2 #nb combinations
    return n