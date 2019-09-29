# variable names are places where the user is asking Python
# to allocate a bit of memory and stick something in it
# the user chooses the label of the varible known as the variable name

# mnemonic means choosing the variable name that makes sense

# mathematical operations in Python

a = float(raw_input("a: "))
b = float(raw_input("b: "))
# we can use int() and float () to convert between strings and integers
# an error occurs if the string does not contain any neumeric characters

print "addition: ",(a+b) # in print function a comma (,) after a " puts a space 
print "subrtaction (a-b): ",(a-b)
print "product: ",(a*b)
print "division (a/b): ",float(a/b)
print "exponent (a^b): ",(a**b)
print "remainder (a%b): ",(a%b)

print
print "result of (1+2**3/4*5): ",(1+2**3/4*5) # precedence of operators
