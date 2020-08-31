################################################################################
# Strings and Text
################################################################################

type_of_people = 10
x = f"there are {type_of_people} types of people."
#this is an F string which is grabbing value from a variable type_of_people

binary = 'binary'
do_not = "don't"
y = f"those who know {binary} and those who {do_not}"
#inserting the values from the variables into the f string

print(x)
print(y)

print(f"I said: {x}")
#printing out the value from the variable x using f string
print(f"I said: {y}")
#printing out the value from the variable y using f string

hilarious = False #false is a boolean
joke_evaluation = "isn't that joke so funny?! {}"
#has an empty string literal but is not in an f string format


print(joke_evaluation.format(hilarious))
#formating our string and insterting in the empy string literal

w = 'this is the left side of ... '
e = 'a string with a right side'

print(w + e) # concatenation
