""" def permutation(I, C):
    if len(I) == len(C): return [C]
    R = []
    for i in I:
        if i not in C: 
            R.append(permutation(I, C + i))
    return [item for sublist in R for item in sublist]

def middle_permutation(string):
    arr = sorted(permutation(list(string), ''))
    print(arr)
    return arr[int(len(arr) / 2) - 1] """

def middle_permutation(string):
    arr = sorted(list(string))  
    return '{}{}{}'.format(
        arr.pop(int(len(arr) / 2)) if len(arr) % 2 == 1 else '', 
        arr.pop(int(len(arr) / 2) - 1), 
        ''.join(reversed(arr))
    )

print('result = {}'.format(middle_permutation("123")))
print('result = {}'.format(middle_permutation("1234")))
print('result = {}'.format(middle_permutation("12345")))
print('result = {}'.format(middle_permutation("123456")))
print('result = {}'.format(middle_permutation("1234567")))
#print('result = {}'.format(middle_permutation("12345678")))

# 1 2 3 4 5
# 3 - 3 : 1 2 4 5 
# 2 - 2 : 1 4 5
# 3 - 5 : 1 4 
# 2 - 4 : 1 
# 1 - 1

# 1 2 3 4 5 6 7 -> 4 3 7 6 5 2 1 
# 4 : 1 2 3 5 6 7
# 3 : 

# 1 2 3 4 5 6 -> 3 6 5 4 2 1 
# 3 - 3 : 1 2 4 5 6
# 5 - 6 : 1 2 4 5 
# 4 - 4 : 1 2 5
# 3 
# 2
# 1 

""" import math

def middle_permutation(string):
    x = int(math.factorial(len(string)) / 2)
    print(x)
    return sorted(string)



print(middle_permutation("abcde")) # "bac" """

'''
You are given a string s. Every letter in s appears once.

Consider all strings formed by rearranging the letters in s. After ordering these strings in dictionary order, return the middle term. (If the sequence has a even length n, define its middle term to be the (n/2)th term.)
Example

For s = "abc", the result should be "bac". The permutations in order are: "abc", "acb", "bac", "bca", "cab", "cba" So, The middle term is "bac".
Input/Output

    [input] string s

    unique letters (2 <= length <= 26)

    [output] a string

    middle permutation.

'''