#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(f"The number {number} is positive" if number > 0 else f"The number {number} is zero" if number == 0 else f"The number {number} is negative")
