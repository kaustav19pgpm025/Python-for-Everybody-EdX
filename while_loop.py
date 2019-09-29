# Loops (repeated steps) have interation variables that change each time
# through a loop. Often these iteration variables go through a sequence of numbers
# while is an indefinite loop

n = int(raw_input("Enter n: "))
while n > 0:
# as long as the statement is true the statements below will be executed
	n = n - 1
	print n,"\n"
print "Blastoff"

print "value of n after the last iteration",n
