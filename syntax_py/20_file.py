import os # for delete

# Examples
f = open('myfile.txt') # open file with mode r (read)
f = open('myfile.txt', 'rt') # specify open mode
txt = f.read()
txt = f.read(5) # read 5 characters
txt = f.readline() 
for x in f:
    x # return line
f.close()

# Write to existing file. Allowed: 'a', 'w'
f = open('myfile.txt', 'a') # Add text
f.write('New text')
f.close()

f = open('myfile.txt', 'w') # overwrite
f.write('New new text')
f.close

# Create new file. Allowed 'x', 'a', 'w'
f = open('myNewFile1.txt', 'x')
f = open('myNewFile2.txt', 'w')

# delete file
os.remove('myNewFile1.txt')
# delete if exists
if os.path.exists('myNewFile2.txt'):
    os.remove('myNewFile2.txt')

# Directory
if not os.path.exists('myfolder'):
    os.mkdir('myfolder')
os.rmdir('myfolder')

# Modes
# "r"   -   Read - Default value. Opens a file for reading, error if the file does not exist
# "a"   -   Append - Opens a file for appending, creates the file if it does not exist
# "w"   -   Write - Opens a file for writing, creates the file if it does not exist
# "x"   -   Create - Creates the specified file, returns an error if the file exists

# Additional mode
# "t"   -   Text - Default value. Text mode
# "b"   -   Binary - Binary mode (e.g. images)