def get_position(n, arr):
    for sublist in arr: 
        for item in sublist :
            if n in sublist:
                return [arr.index(sublist), sublist.index(n)]
    return None 

def get_nearby(position, arr):
    result = []
    # top, bottom
    for i in range(-1, 2): 
        if position[0] + i >= 0 and position[0] + i <= len(arr) - 1:
            result.append(arr[position[0] + i][position[1]])

    # left, right
    for i in range(-1, 2, 2): 
        if position[1] + i >= 0 and position[1] + i <= len(arr[0]) - 1:
            result.append(arr[position[0]][position[1] + i])
    
    return list(filter(lambda x : x != None, result))

def mixing(arr, s):
    result = []
    for i in range(0, len(arr[0])):
        if len(arr) == 1:
            result.append(s + arr[0][i])
        else:
            result += mixing(arr[1:], s + arr[0][i])
    return result
    
def get_pins(observed):
    # observed - str 
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [None, 0, None]
    ]

    nearby = []
    for item in observed: 
        pos = get_position(int(item), arr)   
        nearby.append(get_nearby(pos, arr)) 

    nearby = list(map(lambda item: list(map(str, item)), nearby)) 
    mixed = mixing(nearby, '')

    return sorted(mixed)

print(get_pins('0'))

""" Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘

He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we count on you!

For C# user: Do not use Mono. Mono is too slower when run your code.
 """