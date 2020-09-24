################################################################################
#Reading Files
################################################################################
#importing argv module to the file
#sys is the module and argv is the script
from sys import argv
# #script is going to have the value of the file name ex15.py
# #file name is going to have the name ex15_sample.txt
# script, filename = argv
# #this is going to open the file and return it as a file object
# txt = open(filename)
# #
# print(f"here's your file {filename}:")
# #I assume that the file is going to be opened and show what is written inside of it
# print(txt.read())
# #once \we type the file name we should be able to see what has been written inside of it
# print("type the filename again:")
# file_again = input("> ")
#  #this is going to open the file
# txt_again = open(file_again)
# #this is going to show what is in the file itself
# print(txt_again.read())
################################################################################
#second attempt to understand reading files
################################################################################
#from sys import argv
#we are accessing our library sys and from there importing our script argv
script, filename = argv
#script is the name of the file we are using when running the script
#filename is the name of the file that we are trying to access during this excercise
txt = open(filename)
#we have a variable called txt which is going to hold the value which allows us
#to open our file once we give our filename a value
print(f"Here's your file {filename}")
#we are using our f-string here to see the name of the file that we are using
print(txt.read())
#here we are seeing that we are reading the document that is written inside the txt file
print("type the filename again:")
#we are asking the user to type in the file name again
file_again = input("> ")
# here is where the user enters in the file name
text_again = open(file_again)
# After file_again entry has been submitted text_again will run and will open up
# our filename that we have entered and read the file
print(text_again.read())
# after text_again has been completed we are going to run the read function and
# read the value of the file aka text
