# multiple elif statements

x = raw_input("Enter value: ")
if x <= 2:
	print "small"
elif x <= 10:
    print "medium"
elif x <= 20:
	print "big"
elif x <= 40:
	print "large"
elif x <= 100:
	print "huge"
else:
    print "enormous"
