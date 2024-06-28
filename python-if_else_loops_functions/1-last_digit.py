#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastD = number % 10
else:
    lastD = (abs(number) % 10) * -1
string = "Last digit of"
if lastD > 5:
    print(f"{string} {number} is {lastD} and is greater than 5")
elif lastD == 0:
    print(f"{string} {number} is {lastD} and is 0")
else:
    print(f"{string} {number} is {lastD} and is less than 6 and not 0")

