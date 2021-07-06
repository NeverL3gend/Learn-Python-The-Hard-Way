# Strings and Text

#We assigned types_of_people with the value of 10
types_of_people = 10
# We assigned x a value of a f String that is going to contain the value of types_of_people
x = f"There are {types_of_people} types of people."
#following should output: There are 10 types of people.

#We assgined binary with a string value. 
binary = "binary"
#We assigned do_not with a string value.
do_not = "don't"
#We assigned y a value of a f String that is going to contain the value of binary and do_not in the string.
y = f"those who know {binary} and those who {do_not}."
#following should output: Those who know binary and those who don't.

print (x)
print (y)

print (f"I said: {x}")
#following should output: I said: There are 10 types of people
print (f"I also said: '{y}'")
#following should output: Those who know binary and those who don't

#We assigned hilarious with a boolean of False
hilarious = False
#We assigned Joke_evaluation with a string which contains an empty bracket which is known as a place holder
joke_evaluation = "Isn't that joke so funny?! {}"
#Here we are printing Joke_evaluation and it is using a format method. Format Method returns formatted String for place holders
print (joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."
#We are concatinating w and e variables
print (w+e)