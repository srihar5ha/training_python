# A Python program to demonstrate use of 
# generator object with next() 

# A generator function
def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3

# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next
print(x.__next__()); # In Python 3, __next__()
print(x.__next__());
print(x.__next__());
