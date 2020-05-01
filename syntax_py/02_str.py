# Text 
x = "Hello world" # str
x = """Multiline
String""" # multiline str
x[1] # get symbol
x[1:3] # slicing
x[-3:-1] # slicing from the end
len(x) # length
x.strip() # remove whitespace from begin and end 
x.lower() # to lower case
x.upper() # to upper case
x.replace('M', 'Q') # replace string occurence in string
x.split('l') # split string by finding separator
'e' in x
'x' not in x
x + " " + x # string concatenation
x = "value 1 = {}, value 2 = {}, value 3 = {}" # string format, combined numbers and string
x = "value 1 = {0}, value 2 = {1}, value 3 = {2:.2f}" # as index can be name
x = x.format(1,2,3.234)
print(x)

# Methods
# capitalize()      -  	Converts the first character to upper case
# casefold()        -  	Converts string into lower case
# center()          -  	Returns a centered string
# count()           -	Returns the number of times a specified value occurs in a string
# encode()          -	Returns an encoded version of the string
# endswith()        -	Returns true if the string ends with the specified value
# expandtabs()      -	Sets the tab size of the string
# find()            -	Searches the string for a specified value and returns the position of where it was found
# format()          -	Formats specified values in a string
# format_map()      -	Formats specified values in a string
# index()           -	Searches the string for a specified value and returns the position of where it was found
# isalnum()         -	Returns True if all characters in the string are alphanumeric
# isalpha()         -	Returns True if all characters in the string are in the alphabet
# isdecimal()       -	Returns True if all characters in the string are decimals
# isdigit()         -	Returns True if all characters in the string are digits
# isidentifier()    -	Returns True if the string is an identifier
# islower()         -	Returns True if all characters in the string are lower case
# isnumeric()       -	Returns True if all characters in the string are numeric
# isprintable()     -	Returns True if all characters in the string are printable
# isspace()         -	Returns True if all characters in the string are whitespaces
# istitle()         - 	Returns True if the string follows the rules of a title
# isupper()         -	Returns True if all characters in the string are upper case
# join()            -	Joins the elements of an iterable to the end of the string
# ljust()           -	Returns a left justified version of the string
# lower()           -	Converts a string into lower case
# lstrip()          -	Returns a left trim version of the string
# maketrans()       -	Returns a translation table to be used in translations
# partition()       -	Returns a tuple where the string is parted into three parts
# replace()         -	Returns a string where a specified value is replaced with a specified value
# rfind()           -	Searches the string for a specified value and returns the last position of where it was found
# rindex()          -	Searches the string for a specified value and returns the last position of where it was found
# rjust()           -	Returns a right justified version of the string
# rpartition()      -	Returns a tuple where the string is parted into three parts
# rsplit()          -	Splits the string at the specified separator, and returns a list
# rstrip()          -	Returns a right trim version of the string
# split()           -	Splits the string at the specified separator, and returns a list
# splitlines()      -	Splits the string at line breaks and returns a list
# startswith()      -	Returns true if the string starts with the specified value
# strip()           -	Returns a trimmed version of the string
# swapcase()        -	Swaps cases, lower case becomes upper case and vice versa
# title()           -	Converts the first character of each word to upper case
# translate()       -	Returns a translated string
# upper()           -	Converts a string into upper case
# zfill()           -	Fills the string with a specified number of 0 values at the beginning