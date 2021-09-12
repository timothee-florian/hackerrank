# https://www.hackerrank.com/challenges/caesar-cipher-1/problem
def caesarCipher(s, k):
    k = k % 26
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    alphabet = alphabet_lower + alphabet_upper
    new_alphabet_lower= alphabet_lower[k:] + alphabet_lower[:k] # rotating
    new_alphabet_upper= alphabet_upper[k:] + alphabet_upper[:k]
    new_alphabet = new_alphabet_lower + new_alphabet_upper
    table = {}
    for i in range(len(new_alphabet)):
        table[alphabet[i]] = new_alphabet[i]
    coded_message = ''.join([table[l] if l in alphabet else l for l in s])
    
    return coded_message