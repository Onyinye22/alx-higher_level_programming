#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(b"{number} is positive")
elif number == 0:
    print(b"{number} is zero")
else:
    print(b"{number} is negative")
