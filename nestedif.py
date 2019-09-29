# nested if statement
# to see whether a number falls in a given rage

x = int(raw_input("Enter value: "));
if x > 50: # in an if-else construct either the if or the else is going to run
	if x < 100:
		print "half century"
	else:
		print "century"
else:
    print "not a half century"
	