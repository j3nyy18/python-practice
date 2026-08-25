#Function to check if a number is prime

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print("The number is prime")
else:
    print("The number is not prime")


#Function to reverse a string

def reverse_string(text):
    return text[::-1]

text = input("Enter a string: ")
print("Reversed String: ", reverse_string(text))


#Function to find factorial

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

number = int(input("Enter a number: "))

print("Factorial of the entered number: ", factorial(number))


#Function to calculate simple interest

def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time in Years: "))

print("Simple Interest: ", simple_interest(principal, rate, time))


#Function to check if a word is palindrome

def is_palindrome(word):
    return word.lower() == word.lower()[::-1]

word = input("Enter a word: ")

if is_palindrome(word):
    print("The word is palindrome")
else:
    print("The word is not palindrome")


#Function to count vowels in a string

def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

text = input("Enter a string: ")
print("Number of Vowels: ", count_vowels(text))


#Function to merge two lists

def merge_lists(list1, list2):
    return list1 + list2

list1 = [1, 2, 3]
print("List1: ", list1)
list2 = [4, 5, 6]
print("List2: ", list2)

merged = merge_lists(list1, list2)

print("Merged list: ", merged)


#Function to find GCD of two numbers

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD:", find_gcd(num1, num2))


#Function to find area of rectangle

def rectangle_area(length, width):
    return length * width

length = float(input("Enter length: "))
width = float(input("Enter width: "))

print("Area of rectangle: ", rectangle_area(length, width))


#Function to check Armstrong number

def is_armstrong(num):
    original = num
    digits = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** digits
        num //= 10

    return total == original


number = int(input("Enter a number: "))

if is_armstrong(number):
    print("The number is Armstrong number")
else:
    print("The number is not Armstrong number")