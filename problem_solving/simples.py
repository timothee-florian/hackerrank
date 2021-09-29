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

# https://www.hackerrank.com/challenges/jim-and-the-orders/problem
# greedy
def jimOrders(orders):
    # Write your code here
    delivery_time = [(sum(x), i) for i, x in enumerate(orders)]
    delivery_time.sort()
    customers = [x[1]+1 for x in delivery_time]
    return customers

# https://www.hackerrank.com/challenges/two-arrays/problem
# greedy
def twoArrays(k, A, B):
    A.sort()
    B.sort()
    B = B[::-1]
    for i in range(len(A)):
        if A[i] + B[i] < k:
                return 'NO'
    return 'YES'

# https://www.hackerrank.com/challenges/marcs-cakewalk/problem
# greedy
def marcsCakewalk(calorie):
    # Write your code here
    calorie.sort()
    miles = 0
    for i, c in enumerate(calorie[::-1]):
        miles += c * 2 ** i
    return miles
# https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
# greedy
def maximumPerimeterTriangle(sticks):
    sticks.sort()
    for i in range(len(sticks)-1, 1, -1):
        if sticks[i] < sticks[i-1] + sticks[i-2]:
            return [sticks[i-2] , sticks[i-1] , sticks[i]]
    return [-1] 

# https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem
# greedy
def decentNumber(n):
    n3 = 0
    n5 = n
    while True:
        if n5 % 3 == 0:
            print('5'*n5 + '3'* n3)
            break
        n5 -= 5
        n3 += 5
        if n3 > n:
            print('-1')
            break

# https://www.hackerrank.com/challenges/priyanka-and-toys/problem
# greedy
def toys(w):
    w.sort()
    i = 0
    n_cont = 0
    while True:
        if i >= len(w):
            break
        min_v = w[i]
        i += 1
        n_cont += 1
        while True:
            if i >= len(w) or w[i] > min_v + 4:
                break
            i += 1

# https://www.hackerrank.com/challenges/largest-permutation/problem
# greedy
# index dictionary
def largestPermutation(k, arr):
    s_arr = sorted(arr)[::-1]
    d_arr = {}
    for i, v in enumerate(arr): # use to find index, faster then .items
        d_arr[v] = i
        
    n_swap = 0
    if s_arr == arr or k >= len(arr):
        return s_arr
    for i in range(len(arr)):
        v = arr[i]
        vs = s_arr[i]
        if v != vs:
            n_swap += 1
            if n_swap > k:
                break
            index1 = d_arr[v]
            index2 = d_arr[vs]
            
            temp = d_arr[v]
            d_arr[v] = d_arr[vs]
            d_arr[vs] = temp
            
            arr[index2] = v
            arr[index1] = vs
    return arr

# https://www.hackerrank.com/challenges/picking-numbers/problem
# implemetation
def pickingNumbers(a):
    # Write your code here
    values = sorted(list(set(a)))
    count_v = {}
    max_length = 0
    for v in a:
        count_v[v] = count_v.get(v, 0) + 1
    for i in range(len(values)):
        max_length = max(max_length, count_v[values[i]])
        if i>= 1 and values[i] - values[i-1] == 1:
            max_length = max(max_length, count_v[values[i]] + count_v[values[i-1]])
    return max_length

# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
# Implemetation
def jumpingOnClouds2(c, k):
    n = len(c)
    energy = 100
    i = 0
    while True:
        energy -= 1
        if c[i] == 1:
            energy -= 2
        i = (i + k)%n
        if i == 0:
            break
    return energy

# https://www.hackerrank.com/challenges/cut-the-sticks/problem
# implementation
def cutTheSticks(arr):
    arr.sort()
    lengths = []
    while len(arr)>0:
        lengths += [len(arr)]
        to_cut= arr.pop(0)
        arr = [a - to_cut for a in arr if a - to_cut > 0]
    return lengths

# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
# implementation
def jumpingOnClouds(c):
    n_jump = 1
    i = 0
    while i +2 < len(c)-1:
        n_jump += 1
        if c[i+2] == 1:
            i += 1
        else:
            i+=2
    return n_jump

# https://www.hackerrank.com/challenges/equality-in-a-array/problem
# implementation
def equalizeArray(arr):
    count_values = {}
    for a in arr:
        count_values[a] = count_values.get(a, 0) +1
    max_sames = 0
    for n in count_values.values():
        max_sames = max(max_sames, n)
    return len(arr) - max_sames

# https://www.hackerrank.com/challenges/acm-icpc-team/problem
# implementation, set, dict, union  
# Strangely brut force works
def acmTeam(topic):
    know = [{i for i, v in enumerate(t) if v == '1'} for t in topic]
    team_known = {}
    for i in range(1, len(topic)):
        for j in range(i):
            team_known[(i, j)] = len(know[i].union(know[j]))
    max_known = 0
    n_team = 0
    for number_known_topic in team_known.values():
        if number_known_topic > max_known:
            max_known = number_known_topic
            n_team = 1
        elif number_known_topic == max_known:
            n_team += 1
    return [max_known, n_team]

# https://www.hackerrank.com/challenges/minimum-distances/problem
# implementation
def minimumDistances(a):
    # Write your code here
    values_indexes = {}
    for i, v in enumerate(a):
        values_indexes[v] = values_indexes.get(v, []) + [i]
    min_distance = float('inf')
    exist = False
    for v in values_indexes.values():
        if len(v)>1:
            min_distance = min(min_distance, max(v)- min(v))
            exist =True
    if exist:
        return min_distance
    return -1

# https://www.hackerrank.com/challenges/happy-ladybugs/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def happyLadybugs(b):
    count_carac = {}
    for l in b:
        count_carac[l] = count_carac.get(l, 0) + 1
    for k, v in count_carac.items():
        if k != '_' and v == 1:
            return 'NO'
    if len(count_carac.keys())==1 and count_carac.get('_', 0) != 0:
        return 'YES'
    if count_carac.get('_', 0) == 0:
        for i in range(1, len(b)-1):
            if b[i] != b[i-1] and b[i] != b[i+1]:
                return 'NO'
    return 'YES'