# 1. Write a program to print your name, age, and city in one line.

name = "Jeny"
age = 22
city = "Chikhli"
print (f"Name: {name} , Age: {age}, City: {city}")


# 2. Take user input for two numbers and print their sum.

a = int (input ("Enter Number 1: "))
b = int (input ("Enter Number 2: "))
print("The sum of 2 number: ", a+b)

# 3. Write a program to convert temperature from Celsius to Fahrenheit.

c = float (input ("Enter the Temperature in Celsius: "))
f = (c * 9 / 5) + 32
print("Entered Temperature in Fahrenheit: ", f)

# 4. Store your name in a variable and print it in uppercase.

name = "Jeny"
print ("Name in uppercase: ", name.upper())

# 5. Ask the user for their birth year and calculate their current age.

current_year = 2026
birth_year = int (input ("Enter your birth year: "))
age = current_year - birth_year
print ("Your Current Age: ", age)

# 6. Write a program to swap the values of two variables.

num1 = int (input ("Enter number 1:"))
num2 = int (input ("Enter number 2:"))
num1 , num2 = num2 , num1
print ("Swapping the numbers")
print ("Number 1: ",num1)
print ("Number 2: ",num2)

# 7. Create a program to calculate the area of a rectangle from user inputs.

length = int (input ("Enter the Lenght of the Rectangle : "))
width = int (input ("Enter the Width of the Rectangle: "))
area = length*width
print ("Area of Rectangle: ", area)

# 8. Write a program to check if a number is positive or negative.

num = int (input ("Enter a Number: "))
if num > 0: 
    print ("Number is Positive")
elif num < 0:
    print ("Number is Negative")
else: 
    print("Number is Zero")

# 9. Ask for two numbers and print their average.

num1 = int (input ("Enter number 1: "))
num2 = int (input ("Enter number 2: "))
avg = (num1 + num1)/2
print("Average of the 2 numbers: ", avg)