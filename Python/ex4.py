################################################################################
#Variables and Names
################################################################################
# the = (equal sign) is a assignment operator. basically assigning a variable a value
# the _ (underscore) is a imaginary space 
cars = 100
space_in_a_car = 4.0 #if you using a floating number or an integer the answer will still come out the same
drivers = 30
passengers = 90
cars_not_driven = cars - drivers  # cars = 100 and drivers = 30 the answer to cars not driven is 70
cars_driven = drivers #Driven cars are 30
carpool_capacity = cars_driven * space_in_a_car #120 is the expected answer
average_passengers_per_car = carpool_capacity / cars_driven # expected answer is 2

#Answers
print('there are', cars, 'cars available')
print('there are only', drivers , 'drivers available')
print('there will be', cars_not_driven, 'empty cars today')
print('we can transport', carpool_capacity, 'people today')
print('we have', passengers, 'to carpool today')
print('we need to put about', average_passengers_per_car, 'in each car')
print(carpool_capacity)
