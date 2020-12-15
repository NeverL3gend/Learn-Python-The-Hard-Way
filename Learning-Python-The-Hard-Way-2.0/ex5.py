# -*- coding: utf-8 -*-
##########################################
#Exercise 5: More Variables and Printing
##########################################
my_name = 'alex'
my_age = '25'
my_height =  72
my_weight = 240
my_eyes = 'brown'
my_teeth = 'white'
my_hair = 'Brown'

print (f"let's talk about {my_name}.")
print (f"He's {my_height} inches tall")
print (f"He's {my_weight} pounds heavy")
print (f"Actually that's not too heavy")
print (f"he's got {my_eyes} eyes and {my_hair} hair")
print (f"his teeth are usually {my_teeth} depending on the coffee")
#this gets tricky
total = my_age, my_height, my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
