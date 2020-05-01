# creating of functions
def func():
    print('hello world')

func()

# multiple arguments
def func1(*args):
    # args - tuple
    print(args)

func1('a', 'b', 'c')

# keyword arguments
def func2(c, b, a):
    print(a + b + c)

func2(a = '1', b = '2', c = '3')

# multiple keyword arguments
def func3(**kwargs):
    print(kwargs['a'] + kwargs['b'])

func3(a = 'A', b = 'B')

# default parameter
def func4(a = 'a'):
    print(a)

func4()

# list of arguments
def func5(myList):
    print(myList)

func5(['a', 'b', 'c'])

# return value
def func6():
    return 1

print(func6())

# empty function
def func7():
    pass

func7()

# recursion
def recursionFunc(a):
    print(a)
    if a != 0: 
        recursionFunc(a - 1)

recursionFunc(3)