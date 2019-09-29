# using if else statement
# to check wheather a number of greater/lesser than or equal to a given number
# only 1 of the conditions will run and the other 2 will not run

x = int(raw_input("Enter benchmark number: "))
n = int(raw_input("Enter number to be checked: "))

if n < x:
    print n,"is less than ",x
elif n == x:
    print n," is equal to ",x
else:
    print n," is greater than ",x
