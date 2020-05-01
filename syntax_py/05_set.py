# Set - unordered, unindexed, No duplicates

# Constructor
x = set(('chair', 'dog', 'apple')) # using build in function
x = set({'a', 'b'})
x = {'a', 'b', 'c'}

# Example
# impossible access by index
x.add('d') # add one item
x.update(['e', 'f', 'g']) # add multiple items
x.remove('g') # remove item
x.discard('f') # remove item
x.pop() # remove last item
x.clear() # clear the set
# del x # delete set
x.union({'x','y', 'z'}) # return set two sets
x.update({'q', 'w'}) # join two sets
set(('chair', 'dog', 'apple')) # constructor

# Methods
# add()                 -	adds an element to the set
# clear()               -	removes all the elements from the set
# copy()                -	returns a copy of the set
# difference()          -	returns a set containing the difference between two or more sets
# difference_update()   -	removes the items in this set that are also included in another, specified set
# discard()             -   remove the specified item
# intersection()        -   returns a set, that is the intersection of two other sets
# intersection_update()	-   removes the items in this set that are not present in other, specified set(s)
# isdisjoint()          -   returns whether two sets have a intersection or not
# issubset()            -   returns whether another set contains this set or not
# issuperset()          -   returns whether this set contains another set or not
# pop()                 -   removes an element from the set
# remove()              -   removes the specified element
# symmetric_difference() -	returns a set with the symmetric differences of two sets
# symmetric_difference_update() -   inserts the symmetric differences from this set and another
# union()               -   return a set containing the union of sets
# update()              -   update the set with the union of this set and others

# frozenset
x = frozenset({'a', 'b', 'c'}) 