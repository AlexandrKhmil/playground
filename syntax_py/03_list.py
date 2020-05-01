# List - ordered, changeable. Allows duplicate

# Constructor
x = list(['a', 'b', 'c', 'd', 'e', 'f']) # using build-in function
x = ['a', 'b', 'c', 'd', 'e', 'f'] 

# Example
x[0]
x[-1]
x[1:4] # from 1 to 4(unincluded) element
x[:4] # from 0 element to 4(unincluded) element
x[1:] # from 1 element to the end
# loop
for a in x: 
	a
# Check if in 
if 'a' in x:
	True
len(x) # length
x.append('new') # add new item
x.insert(1, 'new') # add item at specifix index
x.remove('b') # remove item from list
x.pop(1) # remove last or item indexed
x.pop()
#del x # remove list
del x[1] # remove element by index or all list
#x.clear() # clear list (only for python 3.3+)
#x1 = x.copy() # copy of list (only for python 3+)
x1 = list(x) # copy of list
x1 + x # join two lists
x.extend(x1) # add elements from one list to another
x1 = list(('a', 'b', 'c')) # creating new list by using constructor

# Methods
# append()	-   Adds an element at the end of the list
# clear()	-   Removes all the elements from the list
# copy()	-   Returns a copy of the list
# count()	-   Returns the number of elements with the specified value
# extend()	-   Add the elements of a list (or any iterable), to the end of the current list
# index()	-   Returns the index of the first element with the specified value
# insert()	-   Adds an element at the specified position
# pop()	    -   Removes the element at the specified position
# remove()	-   Removes the item with the specified value
# reverse()	-   Reverses the order of the list
# sort()	-   Sorts the list

# range
x = range(5) 