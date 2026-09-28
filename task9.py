#Write a program to handle division by zero error.
try:
   dividend = int(input("Enter the dividend: "))
   divisor = int(input("Enter the divisor: "))
   result = dividend / divisor
   print(f"Result of division: {result}")
except ZeroDivisionError:
   print("ZeroDivisionError: Cannot divide by zero.")
except ValueError:
   print("ValueError: Invalid input! Please enter valid integers!")

#Write a program to handle invalid integer input.
try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)
except ValueError:
    print("ValueError: Please enter a valid integer!")

#Write a program to open a file and handle the "file not found" error
try:
    with open("sample.txt", "r") as file:
        content = file.read()
    print("File contents:")
    print(content)
except FileNotFoundError:
    print("FileNotFoundError: File not found!")

#Write a program to demonstrate multiple exception blocks.
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("ValueError: Please enter valid integers.")
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero")

#Write a program to use finally for resource cleanup.
try:
    file = open("sample.txt", "r")
    content = file.read()
    print("File contents:")
    print(content)
except FileNotFoundError:
    print("Error: File not found")
finally:
    try:
        file.close()
        print("File closed successfully.")
    except:
        print("File was not opened")

#Write a program to create a custom exception for invalid age (<18).

class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    print("You are eligible.")
except InvalidAgeError as e:
    print("InvalidAgeError:", e)
except ValueError:
    print("ValueError: Please enter a valid age")

#Write a program to handle IndexError when accessing a list.

numbers = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter an index: "))
    print("Value:", numbers[index])
except IndexError:
    print("IndexError: Index is out of range")
except ValueError:
    print("ValueError: Please enter a valid integer index")

#Write a program that takes two numbers and handles all possible errors.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result: ", result)
except ValueError:
    print("ValueError: Please enter valid numbers")
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero")
except Exception as e:
    print("Unexpected error(Exception):", e)

#Write a program to log errors to a file instead of printing them.
try:
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except Exception as e:
    with open("error.log", "a") as file:
        file.write(f"Error: {e}\n")
    print("An error occurred. The error has been logged")

#Write a program that validates an email format and raises an exception for invalid ones.

class InvalidEmailError(Exception):
    pass
try:
    email = input("\nEnter your email: ")
    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email format")
    print("Email is valid.")
except InvalidEmailError as e:
    print("InvalidEmailError:", e)

    