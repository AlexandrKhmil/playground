# Dict - unordered, changeable, indexed. No duplicate
# Constructor
x = dict(a = 'a', b = 'b', c = 'c') # using build-in function
x = {
	'a' : 'a', 
	'b' : 'b',
	'c' : 'c',
	'd' : 'd'
} 

# Example
x['a'] # access item
x.get('a') # access item
# when loop thorugh, returns key value
x.values() # return values of dict
x.items() # returns a list containing a tuple for each key value pair
x.pop('a') # remove item by specified key
x.popitem() # remove last (py 3.7+ remove random)
del x['b']
x.clear() # cler dict 
a = x.copy() # copy dict
a = dict(x) # copy dict by using constructor
a = dict(a = 'a', b = 'b', c = 'c') # dict cunstructor

# Methods
# clear()       -	Removes all the elements from the dictionary
# copy()        -	Returns a copy of the dictionary
# fromkeys()    -	Returns a dictionary with the specified keys and values
# get()	        - 	Returns the value of the specified key
# items()	    - 	Returns a list containing a tuple for each key value pair
# keys()	    - 	Returns a list containing the dictionary's keys
# pop()	        - 	Removes the element with the specified key
# popitem()	    - 	Removes the last inserted key-value pair
# setdefault()  - 	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    - 	Updates the dictionary with the specified key-value pairs
# values()	    - 	Returns a list of all the values in the dictionary