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

"""j = 1;
for i in range (0, len(numbers) - 1):
    temp = numbers[j]
    if (numbers[j] > numbers[j+1]):
        numbers[j] = numbers[j+1]
        numbers[j+1] = temp
        j = j - 1
    j = j + 1
while j < (len(numbers)-1):
    temp = numbers[j]
    if (numbers[j] > numbers[j+1]):
        numbers[j] = numbers[j+1]
        numbers[j+1] = temp
        j = j - 1
    j = j + 1"""
numbers.sort()
half = len(numbers)/2
if (half is int):
    middle1 = numbers[half-1]
    middle2 = numbers[half]
    median = (middle1 + middle2)/2
else:
    half = int(half)
    median = numbers[half]
print(numbers)
print(median)
