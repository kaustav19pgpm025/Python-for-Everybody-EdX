# continue statement ends the current iteration and jumps to the top
# of the loop and starts the next iteration
while True:
    str = raw_input("Enter string: ")
    if str == "skip for continue":
        continue
    if str == "done":
        break
    str = str.upper()
    print str
print "Program done!"
    



