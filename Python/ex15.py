################################################################################
#Reading Files
################################################################################
#importing argv module to the file
#sys is the module and argv is the script
from sys import argv
#script is going to have the value of the file name ex15.py
#file name is going to have the name ex15_sample.txt
script, filename = argv
#this is going to open the file and return it as a file object
txt = open(filename)
#
print(f"here's your file {filename}:")
#I assume that the file is going to be opened and show what is written inside of it
print(txt.read())
#once we type the file name we should be able to see what has been written inside of it
print("type the filename again:")
file_again = input("> ")
 #this is going to open the file
txt_again = open(file_again)
#this is going to show what is in the file itself
print(txt_again.read())
