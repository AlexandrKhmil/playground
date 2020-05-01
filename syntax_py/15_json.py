import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x) # parse to dict

x = {
    'a': 'a',
    'b': 'b',
    'c': 'c'
}
y = json.dumps(x) # parse to json string
y = json.dumps(x, indent=4) # add tabs
y = json.dumps(x, indent=4, separators=('. ', '= ')) # change separators
y = json.dumps(x, indent=4, sort_keys=True) # order

# Allowed types:
# dict      -   Object 
# list      -   Array
# tuple     -   Array
# string    -   String
# int       -   Number
# float     -   Number
# True, False   -   true, false
# None      -   null
