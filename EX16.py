# Reading and Writing Files

# List of Reading and Writing File Methods

#close: Closes the files. Like File-> Save ... in your editor
#read: Reads the contents of the file. You can asisign the result to a variable
#readline: Reads just one line of a text file.
#truncate: Empties the file. Watch out if you care about the file.
#write: Empties the file. Watch out if you care about the file.
#seek(0): Moves the read/write  location to the beginning of the file.

from sys import argv
script, filename = argv

print (f"we're going to erase {filename}.") # when running the script make sure that you enter in the name of the file that we are entering in
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN") # hit enter to start the working with the file

input("CTRl-C Or RETURN?") # asking for an input that is going to either allow us to work with the file or not

print ("Opening the file ... ") # once you hit enter we are going to start opening the file
target = open(filename, 'w') #open("W") is meaning that the file is open for writing, truncating the file first

print ("Truncating the file. Goodbye!") # we are going to clear out the file of the existing content
target.truncate() # this is going to empty the file 

print ("Now I'm going to ask you for three lines.") # we are going to ask for inputs where the user is going to start writing in the file

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file.")

target.write('{}\n{}\n{}\n'.format(line1, line2, line3))

target.write(line1) # write method is going to allow us to write the inputs that the user has entered in, into the test.txt file
target.write("\n") # new line
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("and finally, we close it.")
target.close() # closes the file and saving whatever is in the file
