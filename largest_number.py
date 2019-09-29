# find the largest number
# using largest-so-far method

numbers = list()
n = 0
largest = None

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
    if numbers[i] > largest:
       largest = numbers[i]
print "largest number:", largest
