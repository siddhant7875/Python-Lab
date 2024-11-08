# Program to convert kilometers to miles

# Step 1: Take distance in kilometers as input from the user
# We use float to allow decimal values, as distances can be fractional
kilometers = float(input("Enter distance in kilometers: "))

# Step 2: Define the conversion factor from kilometers to miles
conversion_factor = 0.621371

# Step 3: Calculate the distance in miles
# Multiplying kilometers by the conversion factor to get miles
miles = kilometers * conversion_factor

# Step 4: Displaying the result
print(f"\n{kilometers} kilometers is equal to {miles:.2f} miles.")
