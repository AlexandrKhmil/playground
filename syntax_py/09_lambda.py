# Lambda function - anonymous function, only one expression
x = lambda a : a + 10
print(x(5))

x = lambda a, b: a + b
print(x(5, 10))

def myFunc(n):
    return lambda a : a * n

myFunction = myFunc(2)
print(myFunction(10))
