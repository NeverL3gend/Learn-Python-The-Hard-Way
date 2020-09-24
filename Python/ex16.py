################################################################################
# Reading and Writing Files
################################################################################

from sys import argv

# script, filename = argv
# #when we go into PS we will enter the name of the file and the text file
# #after that we will get instructions if we want to cancel the process or proceed
# print(f"We're going to erase {filename}.")
# print("If you dont want that, hit CTRL-C (^C).")
# print("If you do not want that, hit RETURN.")
#
# #This is expecting us to decide to hit enter or CTRL-C
# input("?")
#
# #once we hit ENTER / RETURN the file will open
# print("opening the file ...")
# target = open(filename, 'w')
#
#
# print("truncating the file. Goodbye!")
# #here the truncate is doing is just deleting the file
# target.truncate()
#
# print("Now I'm going to ask you for three lines")
# #for the next three lines we are entering words into the empty document
# line1 = input("line1: ")
# line2 = input("line2: ")
# line3 = input("line3: ")
#
# print("I'm going to write these to the file")
# #here we are entering in the information we wrote above and writing it into the empty document
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
# #
# opener = open(filename)
# print(opener.read())
################################################################################
#Second attempt to understand what is going on with this section
################################################################################
script, filename = argv
# close: closes the file/saves the document in the state that it is in
# read: reads the content that is in the file. you can assign the result to a variable
# truncate: deletes the content from the file.
# write (' stuff '): writes 'stuff' in the file
# seek(0): moves the read/write location to the beginning of the file

#once we write out our script and file name the f string to going to recognize the file we are talking about
print(f"We're going to erase {filename}")
print('If you do not want that, hit CTRL-C (^C)')
print('If you do want that, hit return')

input("?")
#once the following questions have been answered it will either move forward with the script or cancel it
#once you hit enter the file will begin to open using the opening function
print("opening the file...")
#using the opening function the quotes on the W is allowing the file to be edited or creates a file that does not exist
target = open(filename, 'w')

print('Trunacting the file. goodbye!')
#target is known as the filename here and using the truncate function
#truncate is going to remove all the text information within the file
target.truncate()

print("Now I'm going to ask you for three lines.")
#here we are going to enter some new information in the file
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write thesse to the file.")
# then the information that we written in the lines above will be written
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
#closing the file will save all the information that is written in the document
target.close()
