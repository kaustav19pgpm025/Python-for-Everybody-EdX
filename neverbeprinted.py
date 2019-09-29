# which code will never be printed

# snippet 1
if x < 2:
	print "less than 2"
elif x => 2:
	print "2 or more than 2"
else:
	print "something else" # this code will never run as the conditions of x are already executed 
    
# snippet 2
if x < 2:
    print "less than 2"
elif x < 20:
    print "less than 20"
elif x < 10:
    print "less than 10" # this code will never run as any value <10 is <20
 else:
    print "something else"
    
 
	
	