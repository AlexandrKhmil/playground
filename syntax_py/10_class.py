# class - object constructor
# self - reference to current instance of the class
class MyClass:
    x = 5
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def myFunc(self):
        print(self.a)

p1 = MyClass('A', 'B')
print(p1.x)
print(p1.a + p1.b)
p1.myFunc()

p1.x = 10 # modify object
del p1.b # delete object, only in instance
del p1 # delete object

# empty class
class MyClass1: 
    pass

