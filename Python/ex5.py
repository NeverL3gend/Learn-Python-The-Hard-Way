################################################################################
# More Variables and Printing
################################################################################

my_name = 'Alex Garcia'
my_age = 25
my_height = 75 #inches
my_weight = 240 #lbs
my_eyes = 'Brown'
my_teeth = 'white'
my_hair = 'brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"Actually that is not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")


## how to convesrt lbs to kg
pounds = float(input('enter weight in pounds to conver to kilograms'))
kilo_grams = pounds * 0.453592
print(pounds, 'punds are equal to', kilo_grams,'kilograms')
