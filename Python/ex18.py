################################################################################
# Names, Variables, Code, Functions
################################################################################

#Functions do three things
# 1. They name pieces of code the way variables name strings and numbers
# 2. They take arguments the way your scripts take argv
# 3. Using 1 and 2. They let you make your own "mini-scripts" or "tiny commands"

#EX1: This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
this
#EX2: Ok that *arg is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#EX3: This one takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#EX4: This one takes no argument
def print_none():
    print("I got nothing")

print_two("zed", "shaw")
print_two_again("zed", "shaw")
print_one("first!")
print_none()
