# https://www.hackerrank.com/challenges/flipping-bits/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous
def flippingBits(n):
    # Write your code here
    binary = bin(n)[2:]
    binary = '0' * (32-len(binary)) + binary
    flip_binary = ''.join(['1' if b == '0' else '0' for b in binary])
    return int(flip_binary, 2)