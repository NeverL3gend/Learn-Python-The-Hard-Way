################################################################################
# More Files
################################################################################

from sys import argv
from os.path import exists
#three arguments script from and to
script, from_file, to_file = argv

print(f"copying from {from_file} to {to_file}")

#we could do these two on one, line how?
#it is going to open the file and read the information that is stored in it
in_file = open(from_file)
indata = in_file.read()
#len is going to count string size within the file
print(f"the input file is {len(indata)} bytes long")
# checking if the file exist - maybe return a boolean?
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit return to continue, CTRL-C to abort")
input() #expecting an input from me

# opens the document and making sure that it is in a writable state
out_file = open(to_file, 'w')
# writes the information from "from_file" into "to_file"
out_file.write(indata)

print("alright all done")
#saves both files
out_file.close()
in_file.close()
