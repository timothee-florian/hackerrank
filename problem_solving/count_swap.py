# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
def countSwaps(a):
    # Write your code here
    c = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                c += 1
    print('Array is sorted in {} swaps.'.format(c))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[-1])) 