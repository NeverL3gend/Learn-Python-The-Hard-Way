# Parameter, Unpacking, Variables

#import is  a way to add features to your script
from sys import argv
# read the WYSS section for how to run this 
script, first, second, third = argv

print ("the script is called:", script)
print ("Your first  variable is:", first)
print ("your second variable is:", second)
print ("your third variable is:", third)

# In order to run this file you need to go into the terminal do the following: python EX13.py First, Second, Third
# Once that is done you can run it then you will see First Second and Third printed
# you can replace those with random stuff
# if you input more that what is being asked then you'll run into an error
# if you just try to run the program with no arguments then you're going to run into issues\
