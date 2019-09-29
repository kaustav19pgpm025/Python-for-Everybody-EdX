# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done'
# is entered, print out the largest and smallest of the numbers. If the user enters anything other than
# a valid number catch it with a try/except and put out an appropriate message and ignore
# the number. Enter 7, 2, bob, 10, and 4 and match the output

numbers = list()
n = 0
largest = None
smallest = None

# Entering values in a list
while True:
    val = raw_input("Enter value: ")
    if val == "done":
        break
    # to catch values that are not integers
    # use of try and except block
    try:
        val = int(val)
    except:
        print "Invalid input"
        continue
    numbers.append(val)
# print numbers

# Finding the largest number
n = len(numbers)
# number of values in the list
for i in range (0,n):
    if numbers[i] > largest: # condition to check the largest number
       largest = numbers[i]
print "Maximum is", largest

# Finding the smallest number
# The None keyword is used to define a null value, or no value at all.
# None is not the same as 0, False, or an empty string. None is a
# datatype of its own (NoneType) and only None can be None

# Python has an "is" keyword that can be used in logical expressions. It implies
# "is the same as". It is similar to "==" but not stronger than it. It is
# not a logical operator
for i in range (0,n):
    if smallest is None:
        smallest = numbers[i]
    elif numbers [i] < smallest: # condition to check the smallest number
       smallest = numbers[i]
print "Minimum is", smallest
