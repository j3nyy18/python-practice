#1 Calculate the remainder of two numbers.

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
remainder = num1 % num2
print("Remainder of the numbers: ", remainder)

#2 Check if a number is even or odd.

num = int (input("Enter the Number:"))
if num % 2 == 0: 
    print("Number is Even")
else:
    print("Number is Odd")


#3 Compare two numbers and print the larger one.

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
if num1 > num2:
    print ("Larger Number: ", num1)
elif num2 > num1:
    print ("Larger Number: ", num2)
else:
    print("Both numbers are equal")


#4 Write a program to calculate the square and cube of a number.

num = int(input("Enter the Number: "))
square = num ** 2
cube = num ** 3
print("Square of the Number: ", square)
print("Cube of the Number: ", cube)

#5 Check if two entered numbers are equal.

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
if num1 == num2:
    print("Both are equal numbers")
else:
    print("Both aren't equal numbers")

#6 Take two numbers and print True if both are positive, else False.

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
result= num1 > 0 and num2 > 0
print ("Are both numbers positive? ", result)

#7 Write a program to convert float to integer.

num = float (input ("Enter any decimal number: "))
print ("Decimal number (float) converted to Interger (int): ", int(num))

#8 Take a number as string, convert to int, and multiply by 10.

num = input("Enter a number: ")
num = int(num)
result = num * 10
print("Result: ", result)

#9 Write a program that uses and & or operators to check multiple conditions.

num = int(input("Enter a number: "))

if num > 0 and num < 100:
    print("Number is Positive and less than 100")

if num < 0 or num > 100:
    print("Number is either Negative or greater than 100")


#10 Divide two numbers and print the quotient and remainder separately.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

quotient = num1 // num2
remainder = num1 % num2

print("Quotient: ", quotient)
print("Remainder: ", remainder)
