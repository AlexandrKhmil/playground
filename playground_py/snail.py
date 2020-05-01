def snail(snail_map):
    result = []
    h = len(snail_map)
    w = len(snail_map[0])
    end = dict(right = w, down = h, left = -1, top = -1)
    direction = 'right'
    x, y = (0, 0)
    while len(result) != w * h: 
        result.append(snail_map[y][x])
        if direction == 'right':
            if x + 1 == end['right']:
                direction = 'down'
                end['top'] += 1
                y += 1
            else: 
                x += 1
        elif direction == 'down':
            if y + 1 == end['down']:
                direction = 'left'
                end['right'] -= 1
                x -= 1 
            else:
                y += 1 
        elif direction == 'left':
            if x - 1 == end['left']:
                direction = 'top'
                end['down'] -= 1
                y -= 1  
            else:
                x -= 1 
        else:
            if y - 1 == end['top']:
                direction = 'right'
                end['left'] += 1
                x += 1
            else:
                y -= 1 
    return result
        

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(snail(array)) # [1,2,3,6,9,8,7,4,5]

'''
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

This image will illustrate things more clearly:

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

'''