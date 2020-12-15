##########################################
#Exercise 8: Printing, Printing
##########################################

formatter = " {} {} {} {} "

print (formatter.format(1,2,3,4)) #going to display 1234
#going to display 1234
print (formatter.format('one','two','three','four'))
#going to show true false
print (formatter.format(True, False, True, False))
#going to 16 curly brackets
print (formatter.format(formatter, formatter, formatter, formatter))
#its going to show everything except testing since there are no empty brackets
#after the fourth one
print (formatter.format(
    "going to try and",
    "enter",
    "my own words here",
    "testing beyond 5"
    "testing"
))
