name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
height_cm = height * 2.54
weight = 180  # lbs
weight_kg = weight * 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}")
print(f"He's {height} inches tall")
print(f"He's {weight} pounds heavy")
print(f"Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height} and {weight} I get {total}")

# weight in cm and height in kg
print(f"{height} inches are {round(height_cm)} centimeters.")
print(f"{weight} pounds are {round(weight_kg)} kilograms.")
