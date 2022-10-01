"""Median calculator."""

import math

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

if(len(numbers) % 2 != 0): # If the length of the list is odd.
    middleNumber = math.floor(len(numbers) / 2)
    median = numbers[middleNumber]
else: # If the length of the list is even.
    firstMiddleNumber = numbers[int((len(numbers) / 2) - 1)] # Get left hand side of middle.
    secondMiddleNumber = numbers[int((len(numbers) / 2))] # Get right hand side of middle.

    mean = (firstMiddleNumber + secondMiddleNumber) / 2
    median = mean

print(median)
