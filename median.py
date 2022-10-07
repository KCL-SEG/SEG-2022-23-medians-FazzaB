"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
for num in numbers:
    temp = numbers[i]
    if (numbers[i] > numbers[i+1]):
        numbers[i] = numbers[i+1]
        numbers[i+1] = temp
half = len(numbers)/2
if (half is int):
    middle1 = numbers[half-1]
    middle2 = numbers[half]
    median = (middle1 + middle2)/2
else:
    half = int(half)
    median = numbers[half]
print(numbers)
