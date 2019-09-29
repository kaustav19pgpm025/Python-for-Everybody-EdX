# counting number of values in a loop
# summing up of values in a loop
# average of values in a loop
# filtering in a loop
# using boolean in a loop

numbers = list()

while True:
    val = raw_input("Enter value: ")
    if val == "done":
        break  
    numbers.append(int(val))
print numbers

sum = 0
n = 0

for i in numbers:
    # filtering in a loop
    # print values > 50
    if i > 50:
        print i," is > 50"
    # using boolean in a loop
    # give message if value is 100 or 200
    if i == 100:
        print "100 is present here! It is a century!"
    if i == 200:
        print "200 is present here! It is a double century!"
    n = n + 1 # count number of values
    sum = sum + i # sum of values
    average = sum/n
    
print "number of values: ",n
print "sum of values is: ",sum
print "average of values is: ",average
