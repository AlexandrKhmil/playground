class A(object): # for py 3+ no need for object
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def f(self):
        print('a = {0}\nb = {1}'.format(self.a, self.b))

class B(A):
    def __init__(self, a, b, c):
        # Parent function will be overrited
        # A.__init__(self, a, b) # bad variant
        super(B, self).__init__(a, b) # for py 2
        #super().__init__(a, b) # for py 3
        self.c = c # add mew properties

    # add new method
    def newMethod():
        print('new method') 

c = B('a', 'b', 'c')
c.f()
