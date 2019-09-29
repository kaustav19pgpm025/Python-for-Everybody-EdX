# find the largest number
# using largest-so-far method

numbers = list()
n = 0
largest = None
smallest = None

# Entering values in a list
while True:
    val = raw_input("Enter value: ")
    if val == "done":
        break  
    numbers.append(int(val))
print numbers

# Finding the largest number
n = len(numbers)
# number of values in the list
for i in range (0,n):
    if numbers[i] > largest: # condition to check the largest number
       largest = numbers[i]
print "largest number:", largest

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
print "smallest number:", smallest

   

    