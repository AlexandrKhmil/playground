myTuple = ('apple', 'banana', 'cherry')
myit = iter(myTuple) # returns a iterator
print(myit)
print(next(myit))
print(next(myit))

# creating an iterator (only for py 3+)
class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self 

	def __next__(self):
		x = self.a 
		self.a += 1
		return x

myClass1 = MyNumbers()
myIter1 = iter(myClass1)
print(next(myIter1))

# __iter__() - returns iterator object 
# __next__() - returns the next item in the sequence

# Stop iteration
class StopIterationClass:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a 
            self.a += 1
            return x 
        else:
            raise StopIteration

myClass2 = StopIterationClass()
myIter2 = iter(myClass2)
for x in myIter2:
    print(x)