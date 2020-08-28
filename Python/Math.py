################################################################################
#Python Numbers, Type Conversion and Mathmatics
################################################################################

#Python Supports integers,floating-point numbers and complex numbers. They are
#defined as int, float, and complex classes in Python

# difference between floating and integers is that 5 is an integer while 5.0 is a float
# the decimal is what makes them different

#complex numbers are written in the form of  X + yj, where X is the real part and
# y is the imaginary part

# type() function helps us know which class a variable or a value
# isinstance() function helps us check something belongs to a specific class

#Example


#type() is very similar towards typOf() where you are trying to identify what
#type of data is being used, string, int, floating, complex, etc..
a = 5
print(type(a))
print(type(5.0))

c = 5 + 3j

print(c + 3)
print(isinstance(c, complex))
