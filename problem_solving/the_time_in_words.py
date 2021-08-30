
# https://www.hackerrank.com/challenges/the-time-in-words/problem
def timeInWords(h, m):
    # Write your code here
    time_letter = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fiften', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']

    if m == 0:
        return time_letter[h-1] + " o' clock"
    elif m==1:
        return 'one minute past ' + time_letter[h-1]
    elif m == 59:
        return 'one minute to' + time_letter[h]
    elif m==15:
        return 'quarter past ' +  time_letter[h-1]
    elif m == 30:
        return 'half past ' +  time_letter[h-1]
    elif m == 45:
        return 'quarter to ' +  time_letter[h]
    elif m < 30:
        if m > 20:
            return time_letter[-1] +' '+ time_letter[m-20 -1] + ' minutes past ' + time_letter[h-1]
        else:
            return time_letter[m-1] + ' minutes past ' + time_letter[h-1]
    else:
        if m>40:
            return time_letter[60 - m-1] + ' minutes to ' + time_letter[h]
        else:
            return time_letter[-1] +' '+  time_letter[40 - m-1] + ' minutes to ' + time_letter[h]
