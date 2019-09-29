# count the number of lines in a text file

name = raw_input("enter file name ****.txt: ")
fh = open(name)

count = 0

for line in fh:
    line = line.rstrip()
    count = count + 1
    
print "number of lines in ",name," is: ",count
    
