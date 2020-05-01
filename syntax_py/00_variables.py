# Console Messages
print("Console Message")

if 5 > 2:
    print("5 > 2")

# Python Variables
x = 5
print(x)

a, b, c = 'a', 'b', 'c'
d = e = 'de'
print(a + b + c + d + e)

def globalVariable():
    global e 
    e = 'global'
    print(e)
    global x # refer to global variable
    x += 1 
    print (x)

globalVariable()

# function inside function
def parentFunction():
    print('This is parent')
    def childFunction():
        print('This is child')
    childFunction()