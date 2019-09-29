# We create a new function using the def keyword followed by optional
# parameters in the parentheses. We indent the body of the function. This defines
# the function but does not execute the body of the function. It just remembers
# the code. Later the function is called to invoke it

# An "argument" is a value we pass into the function as its input when we call the function
# We use arguments so we can direct the function to do different kinds of
# work when we call it different times
# We put arguments in parentheses after the name of the function
# big = max ("hello world"), here "hello world" is the argument of the function max

# A "parameter" is a variable which we use in the function definition. It is a
# "handle" that allows the code in the function to access the arguments for
# a particular function invocation. We can use different parameters to the
# function each time it is invoked

# Often a function will take arguments, do some computation and "return" a value to be used
# as the value of the function call in the calling expression. The "return" keyword is
# used for this
# def greet ():
# 	return "Hello"
# a "return" statement does 2 things
# 1. It stops the function and returns to the next line
# 2. It determines the residual value

# A "fruitful" function is one that produces a result (or return value)
# a function that do not return any value is called "non-fruitful" function
# The "return" statement ends the function and sends back the result of the function 
# A "return" statement is the end of execution of the function

# if the function() uses a "print " statement in the end then no print statement
# is required while invoking the function to print its value
# if the function() uses a "return" statement in the end then a print statement
# is required while invoking the function to print its value

# We can define more than 1 parameter in the function definition
# We simply add more arguments when we call the function
# We match the number and order of arguments and parameters

def add_2_numbers(x,y):
	sum = x + y
	return sum
	
a = float(raw_input("Enter a: "))
b = float(raw_input("Enter b: "))
value = add_2_numbers(a,b)
print "Result is: ",value
