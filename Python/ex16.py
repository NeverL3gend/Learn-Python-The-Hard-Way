################################################################################
# Reading and Writing Files
################################################################################

from sys import argv

script, filename = argv
#when we go into PS we will enter the name of the file and the text file
#after that we will get instructions if we want to cancel the process or proceed
print(f"We're going to erase {filename}.")
print("If you dont want that, hit CTRL-C (^C).")
print("If you do not want that, hit RETURN.")

#This is expecting us to decide to hit enter or CTRL-C
input("?")

#once we hit ENTER / RETURN the file will open
print("opening the file ...")
target = open(filename, 'w')


print("truncating the file. Goodbye!")
#here the truncate is doing is just deleting the file
target.truncate()

print("Now I'm going to ask you for three lines")
#for the next three lines we are entering words into the empty document
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file")
#here we are entering in the information we wrote above and writing it into the empty document
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#
opener = open(filename)
print(opener.read())
# print("And finally, we close it!")
# #here we are closing the file
# target.close()
