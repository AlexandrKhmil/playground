import re
def solution(string, markers):
    split_markers = ''
    for i in markers:
        split_markers += "[\{}].*\n".format(i) + "|"
    s = re.split(split_markers.strip('|'), string + '\n') 
    if len(markers) == 0: 
        r = string
    elif len(s) == 1:
        r = s[0][:-1]
    else:
        r = '\n'.join([item.strip(' ') for item in s])[:-1]
    return r
    #return ''.join([item for item in re.split(split_markers.strip('|'), string + '\n')[:-1]])

#print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])) # "apples, pears\ngrapes\nbananas"
#print(repr(solution("\n§", ["#", "§"])))

#print(repr(solution('.\npears bananas cherries oranges bananas\napples lemons oranges .\napples watermelons', ['?', '=', "'"])))

x = solution("' cherries lemons\nstrawberries apples lemons apples watermelons\navocados = watermelons lemons\navocados\n' cherries", ['?', '#', '^', '-', '=', '.', ','])

print(x)

""" print(repr('\n'.join(
    item.strip(' ') for item in 
    re.split("[?].*\n|[=].*\n|['].*\n|",'.\npears bananas cherries oranges bananas\napples lemons oranges .\napples watermelons'))
)) """
'''
import re
def solution(string,markers): 
    print(repr('string = {}'.format(string)))
    print('markers = {}'.format(markers))
    split_markers = ''
    for i in markers:
        split_markers += '[{}].*\n'.format(i) + '|'
    r = '\n'.join([item.strip() for item in re.split(split_markers.strip('|'), string + '\n')]).strip()
    print(repr(r))
    return r
'''

'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples

The output expected would be:

apples, pears
grapes
bananas

The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

'''