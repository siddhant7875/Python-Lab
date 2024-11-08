# Program to check if a person is eligible to vote
# Converting input to integer as age is typically represented as a whole number
age = int(input("Enter your age: "))

# Step 2: Check if age is 18 or older
# 18 is the minimum legal age for voting eligibility
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
