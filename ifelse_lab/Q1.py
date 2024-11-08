# Program to swap two numbers entered by the user

# Step 1: Taking two numbers as input from the user
# The input function takes input as a string, so we will convert it to an integer
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Step 2: Displaying numbers before swapping
print("\nBefore swapping:")
print("First number:", num1)
print("Second number:", num2)

# Step 3: Swapping the numbers
# Using Python's tuple unpacking feature to swap
num1, num2 = num2, num1

# Step 4: Displaying numbers after swapping
print("\nAfter swapping:")
print("First number:", num1)
print("Second number:", num2)
