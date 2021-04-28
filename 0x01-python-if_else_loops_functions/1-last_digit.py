#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    digit = number * -1
    digit = digit % 10
    digit = digit * -1
else:
    digit = number % 10

print("Last digit of {}".format(number), end=' ')


if digit > 5:
    print("is {} and is greater than 5".format(digit))
elif digit == 0:
    print("is {} and is 0".format(digit))
elif digit < 6 and digit != 0:
    print("is {} and is less than 6 and not 0".format(digit))
