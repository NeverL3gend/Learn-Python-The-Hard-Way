##########################################
#Exercise 4: Variables And Names
##########################################
#cars has a total of 100
cars = 100
#there is a total of 4.0 space in the car
space_in_a_car = 4.0
#there are a total of 30 drivers
drivers = 30
#there are a total of 90 passengers
passengers = 90
#this will give us a total of cars that are not being driven
cars_not_driven = cars - drivers
#this will give us a total of cars being driven
cars_driven = drivers
#this is going to give us a max of passengers that can fit in the car
carpool_capacity = cars_driven * space_in_a_car
#this will tell how many people can fit in the car
average_passenger_per_car = passengers / cars_driven

#going to print out the value of cars which is 100
print ("there are", cars , "cars available1")
#going to print out the value of cars which is 30
print ("there are only", drivers , "drivers available")
#going to print out the value of the cars not being driven which is 70
print ("there will be", cars_not_driven , "empty cars today")
#going to print out the how many people are being transported today which is 120.0
print ("we can transport", carpool_capacity ," people today")
#going to print out 90 passengers
print ("we have", passengers , )
#this is going to print out the average_passenger_per_car value which is going to be 3
print ("we need to put about", average_passenger_per_car, "in each car.")
