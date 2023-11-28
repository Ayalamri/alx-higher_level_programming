#!/usr/bin/python3
import random

# Assign a random signed number to the variable 'number'
number = random.randint(-10000, 10000)

# Print the assigned number
print("Last digit of", number, "is", end=" ")

# Extract the last digit of the number
last_digit = abs(number) % 10

# Check the last digit and print the corresponding message
if last_digit > 5:
    print(str(last_digit) + " and is greater than 5")
elif last_digit == 0:
    print(str(last_digit) + " and is 0")
else:
    print(str(last_digit) + " and is less than 6 and not 0")
