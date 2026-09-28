#Create a custom math module and import it in another file.

import math_operations

print("\n1. CUSTOM MATH MODULE: \n")

print("Addition: ", math_operations.add(10, 5))
print("Subtraction: ", math_operations.subtract(10, 5))
print("Multiplication: ", math_operations.multiply(10, 5))
print("Division: ", math_operations.divide(10, 5))


# Create a module to perform string operations.

import string_operations

print("\n2. STRING OPERATIONS MODULE: \n")

text = input("Enter a string: ")

print("Reversed: ", string_operations.reverse_string(text))
print("Number of vowels: ", string_operations.count_vowels(text))
print("Uppercase: ", string_operations.uppercase(text))
print("Lowercase: ", string_operations.lowercase(text))


#Use random module to generate 5 random integers.

import random

print("\n3. RANDOM INTEGERS: \n")

for i in range(5):
    number = random.randint(1, 100)
    print(number)

#Use datetime module to display current date and time.

from datetime import datetime

print("\n4. CURRENT DATE AND TIME: \n")

current_datetime = datetime.now()
print("Current Date and Time: ", current_datetime)
print("Current Date: ", current_datetime.strftime("%d-%m-%Y"))
print("Current Time: ", current_datetime.strftime("%H:%M:%S"))


#se math module to find factorial of a number.

import math

print("\n5. FACTORIAL: \n")

number = int(input("Enter a number: "))
result = math.factorial(number)

print("Factorial: ", result)


#Create a package shapes with modules for circle and rectangle.

from shapes.circle import area as circle_area
from shapes.circle import circumference

from shapes.rectangle import area as rectangle_area
from shapes.rectangle import perimeter

print("\n6. SHAPES PACKAGE: \n")

radius = float(input("Enter circle radius: "))

print("Circle Area: ", circle_area(radius))
print("Circle Circumference: ", circumference(radius))

length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

print("Rectangle Area: ", rectangle_area(length, width))
print("Rectangle Perimeter: ", perimeter(length, width))

#Import multiple functions from one module and use them.

from math_operations import add, subtract, multiply

print("\n7. IMPORT MULTIPLE FUNCTIONS: \n")

print("Addition: ", add(20, 10))
print("Subtraction: ", subtract(20, 10))
print("Multiplication: ", multiply(20, 10))


# Write a program to shuffle a list using random module.

print("\n8. SHUFFLE A LIST: \n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Before shuffling: ", numbers)

random.shuffle(numbers)
print("After shuffling: ", numbers)

#Write a program to calculate the difference between two dates.

from datetime import datetime

print("\n9. DIFFERENCE BETWEEN TWO DATES: \n")

date1 = input("Enter first date (DD-MM-YYYY): ")
date2 = input("Enter second date (DD-MM-YYYY): ")

date1 = datetime.strptime(date1, "%d-%m-%Y")
date2 = datetime.strptime(date2, "%d-%m-%Y")

difference = abs(date2 - date1)

print("Difference: ", difference.days, "days")


#Use os module to list files in a directory.

import os

print("\n10. LIST FILES IN DIRECTORY: \n")

directory = input("Enter directory path (or press Enter for current directory): ")

if directory == "":
    directory = "."

try:
    files = os.listdir(directory)
    print("Files and folders:")
    for file in files:
        print("-", file)

except FileNotFoundError:
    print("Directory not found.")