# A trick in the function

def addtwo(a, b):
    added = a + b
    return a
	
x = addtwo(2, 7)
print(x)

# the program snippet will print 2 as the "added" result is not print or returned
# 2 or the first paratmeter is returned 