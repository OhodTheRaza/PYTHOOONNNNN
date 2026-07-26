temperature = int(input("Enter the temperature in Celsius:  "))
 
if temperature > 20:
 outfit = 'jacket'
 print("it is a cold day Wear a ", outfit)
else:
 outfit = 't-shirt'
 print("it is a warm day Wear a ", outfit)

raining = input("Is it raining? (yes/no):  ")

if raining == "yes" :
 print("Bring an Umbrella")

wind_speed = int(input("Enter the wind speed in km/h:  "))

if wind_speed > 30:
 needs_windbreaker = "yes"
 print("It is windy today.")
 print("Wear a windbreaker over your", outfit)
else:
 needs_windbreaker = "no"
 print("It is calm today.")
 print("No windbreaker needed over your", outfit)

has_puddles = input("Are there puddles on the ground? (yes/no): ")

if has_puddles == "yes":
 shoes = "boots"
 print("The ground is wet.")
 print("Wear", shoes)
else:
 shoes = "Sneakers"
 print("Ground is Dry")
 print("Wear ", shoes)

 print("")

print("Weather check complete!")

print("------ WEATHER OUTFIT PICKER ------")
print("Temperature:", temperature)
print("Outfit Chosen:", outfit)
print("Raining:", raining)
print("Windbreaker Needed:", needs_windbreaker)
print("Shoes Chosen:", shoes)
print("-----------------------------------")