# Reading Files

# Overall goal is to write a script that is going to allot us to read files

from sys import argv

script, filename = argv

txt = open(filename) # open method, opens the file and prints the content inside it

print (f"Here's your fie {filename}")
print(txt.read()) # read method allows you to read the content of the file
print(txt.close()) # close method, closes file and it does not return a value
print ("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print (txt_again.read())
print (txt_again.close())