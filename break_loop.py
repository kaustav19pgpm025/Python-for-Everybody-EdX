# the "break" statement ends the current loop and jumps to the statement immediately 
# following the loop. It is like a loop test that can happen anywhere in the body
# of the loop

# change from lower case to upper case

while True:
    str = raw_input("Enter string: ")
    if str == "done":
        break
        # break is used to get out of this infinite loop
        # as soon as the break is executed the program control branches off
        # to outside of the loop
        # it gets to the next line immediately after the loop 
    str = str.upper()
    print str
    
print "Program done!"
    



