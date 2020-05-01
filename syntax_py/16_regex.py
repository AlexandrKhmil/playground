import re 

txt = 'The rain in Spain'
x = re.findall('i', txt) # return list of matches
x = re.split('\s', txt) 
x = re.sub('\s', '9', txt)
x = re.search('^The.*Spain$', txt) # return match object (None if not found)
y = x.span() # return tuple, start and end pos
y = x.string # return string passed the function
y = x.group() # part of string where there was a match

# Functions 
# findall 	-   Returns a list containing all matches
# search 	-   Returns a Match object if there is a match anywhere in the string
# split 	-   Returns a list where the string has been split at each match
# sub 	    -   Replaces one or many matches with a string

# Metacharacters
# []    - 	A set of characters         "[a-m]" 	
# \     -	Signals a special sequence  "\d" 	
# .     -	Any character 	            "he..o" 	
# ^     -	Starts with 	            "^hello" 	
# $     -	Ends with 	                "world$" 	
# *     -	Zero or more occurrences 	"aix*" 	
# +     -	One or more occurrences 	"aix+" 	
# {}    - 	Number of occurrences 	    "al{2}" 	
# |     -	Either or 	                "falls|stays" 	
# ()    - 	Capture and group 	

# Special Sequences
# \A 	-   Returns a match if the specified characters are 
#           at the beginning of the string 	
#           "\AThe" 	
# \b 	-   Returns a match where the specified characters 
#           are at the beginning or at the end of a word 	
#           r"\bain" r"ain\b" 	
# \B 	-   Returns a match where the specified characters 
#           are present, but NOT at the beginning (or at the end) 
#           of a word 	
#           r"\Bain" r"ain\B" 	
# \d 	-   Returns a match where the string contains digits 
#           (numbers from 0-9) 	
#           "\d" 	
# \D 	-   Returns a match where the string DOES NOT contain digits
#        	"\D" 	
# \s 	-   Returns a match where the string contains a white space 
#           character 	
#           "\s" 	
# \S 	-   Returns a match where the string DOES NOT contain a white
#           space character 	
#           "\S" 	
# \w 	-   Returns a match where the string contains any word 
#           characters (characters from a to Z, digits from 0-9, 
#           and the underscore _ character) 	
#           "\w" 	
# \W 	-   Returns a match where the string DOES NOT contain any 
#           word characters 	
#           "\W" 	
# \Z 	-   Returns a match if the specified characters are at the end 
#           of the string 	
#           "Spain\Z"

# Sets
# [arn]     -   Returns a match where one of the specified characters (a, r, or n) are present 	
# [a-n]     -   Returns a match for any lower case character, alphabetically between a and n 	
# [^arn]    -   Returns a match for any character EXCEPT a, r, and n 	
# [0123]    -   Returns a match where any of the specified digits (0, 1, 2, or 3) are present 	
# [0-9]     -   Returns a match for any digit between 0 and 9 	
# [0-5][0-9]    -   Returns a match for any two-digit numbers from 00 and 59 	
# [a-zA-Z]  -   Returns a match for any character alphabetically between a and z, lower case OR upper case 	
# [+] 	    -   In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string 	