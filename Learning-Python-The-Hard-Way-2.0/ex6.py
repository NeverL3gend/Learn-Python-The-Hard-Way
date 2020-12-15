##########################################
#Exercise 6: Strings and Text
##########################################
types_of_people = 10
#this is going to place the value of 10 into types_of_people in the f string
x = f"There are  {types_of_people} types of people"

binary = "binary"
do_not = "don't"
#this is going to place the value binary and do_not in the f string
y = f"Those who know {binary} and those who {do_not}"

#this is going to print the f string with the value of 10
print (x)
#this is going to print the f string with the value of binary and don't
print (y)

#this is going to print x with the value of 10
print(f"I said: {x}")
#this is going to print y with the value of binary and don't
print(f"I also said: '{y}'")

hilarious = False

joke_evaluation  = "Isn't that joke funny?! {}"

print(joke_evaluation.format(hilarious))

w = "this is the left side of ... "
e = "a string with a right side."

print(w + e)
