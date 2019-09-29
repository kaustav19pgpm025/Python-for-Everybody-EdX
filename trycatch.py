# try and except structure
# you surround a section of code that may fail with try and except
# if the code in the try block works the except is skipped
# if the code in the try block fails it jumps to the except section

# in try and catch the traceback stops at the line which has raised the exception

# the user needs to compensate for the situations that might cause errors

# the line which has an exception is not a line that is executed succesfully
# the line previous to that line is the last line to be executed succesfully

# try catch is not used in python
# try except is used
name = raw_input ("enter name: ")
age = raw_input("enter age: ")
try:
    age = int(age)
except:
    print "error! write in figures"
    age = -1
    
print name,"is",age,"years old"
    