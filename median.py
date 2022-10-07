"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
def median(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    index = n // 2
    if n % 2:
        return numbers[index]
    else:
        return (sum(numbers[index-1:index+1]))/2

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
medianResult = median(numbers)
print(medianResult)
