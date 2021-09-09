def fizzBuzz(n):
    '''
    for all interger from 1 to n included print:
        FizzBuzz if number is a mulitple of 3 and 5 FizzBuzz
        Fizz if only multiple of 3 and not 5
        Buzz if only multiple of 5 and not 3
        the number otherwise
    '''
    for i in range(1, n+1):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i %5 == 0:
            print('Buzz')
        else:
            print(i)