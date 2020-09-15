################################################################################
#Parameters, Unpacking, Variables
################################################################################
from sys import argv
# read the wyss section for how to run this

# script, first, second, third = argv
#
# print("the script is called:", script)
# print("your first variable:", first)
# print("your second variable:", second)
# print("your third variable:", third)

################################################################################
# Notes
################################################################################
'''
import -> is allows us to add modules to our python file (script) from the
python module set. Python will ask you what module you're planning you use.
This keeps our program small, but ut also acts as a documentation for other devs.
'''
################################################################################

################################################################################
#Study Drill
################################################################################

# script, first, second, third = argv
#
# print("this is called:", script)
#
# print("this is called:", first)

#when i give the script fewer arguments we get an error message that states that there are not enough values

# eat, food, utensels, clock, sky = argv
#
# print('what is this script called:', eat)
# print('what is the first variable called:', food)
# print('what is the second variable called:', utensels)
# print('what is the third variable called:', clock)
# print('what is the fourth variable called:', sky)
#
# food = input('what is your favorite food?') #assigning a variable a value
# #once we provide that value we are
# print("looks like your favorite food is" , food)
#
# utensels = input('what do you use to cut a steak?')
# print('looks like you use', utensels)

################################################################################
# Notes
################################################################################
'''
Looking at the variable eat, food, utensels, clock, sky

when we go into powershell and type out python ex13.py, food, utensels, clock, sky

we are assigning eat to ex13.py which is giving them an assigned value

when we type out  the rest of the food, utensels, clock, sky we can assign them a value

like a,4,5,asdf and eat, food, utensels, clock, sky will be assigned those value

'''
################################################################################

script,testing = argv

print('what script is this:', script)
print('testing argv with less than 3 variables:', testing)


#If you run the file in powershell just by doing python ex13.py you will get an error
#error that you are receiving is that the there is not enough values to unpack(expected2, got 1)
#since we ran the file without assigning testing a value
