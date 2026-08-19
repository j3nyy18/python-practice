
#Check if a person is eligible to vote (age ≥ 18).

age = int (input("Enter your Age: "))
if age >= 18:
    print("You are eligible to vote!")
elif age< 18 and age>0: 
    print("You are not eligible to vote!")
else:
    print("You have entered invalid age!")

#Grade calculator based on marks: 90+ = A, 80+ = B, else C.

marks = int (input("Enter your Marks: "))
if marks > 100:
    print("Your marks must be out of 100 only!")
elif marks >= 90:
    grade = "A"
    print("Your Grade: ", grade)
elif marks >= 80:
    grade = "B"
    print("Your Grade: ", grade)
else:
    grade = "C"
    print("Your Grade: ", grade)

#Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.

def traffic_light(light):
    match light:
        case "Red": return "Stop"
        case "Yellow": return "Wait"
        case "Green": return "Go"
        case _ : return "Invalid Color"
print(traffic_light("Red"))
print(traffic_light("Yellow"))
print(traffic_light("Green"))

#ATM withdrawal check: sufficient balance or not.

balance =int(input("Enter your balance: "))
atm_withdrawal = int(input("Enter your withdrawal: "))
if atm_withdrawal <= balance:
    print("Sufficient balance so Withdrawal successful!")
    balance -= atm_withdrawal
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")

#Check if a number is positive, negative, or zero.

num = int(input("Enter a number: "))
if num >0:
    print("Number is Positive!")
elif num < 0:
    print("Number is Negative!")
else: 
    print("Number is Zero!")

#Check if a number lies within a given range.

num = int(input("Enter a number: "))
lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))
if lower_limit <= num <= upper_limit:
    print("Number lies within the given range!")
else:
    print("Number is outside the given range!")

# Username & password verification.

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "12345":
    print("Login Successful!")
else:
    print("Invalid username or password!! Try Again later!")

# Electricity bill calculator based on units consumed.


# Simple calculator (add, subtract, multiply, divide).

num1 = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = int(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cant divide by zero!")
else:
    print("Invalid Operator!")

# Check type of triangle (equilateral, isosceles, scalene).

side1 = int(input("Enter 1st side: "))
side2 = int(input("Enter 2nd side: "))
side3 = int(input("Enter 3rd side: "))

if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Invalid triangle!")

elif side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
    print("Invalid triangle!")

elif side1 == side2 == side3: #all sides equal
    print("Equilateral triangle")

elif side1 == side2 or side2 == side3 or side1 == side3: #any two sides equal
    print("Isosceles triangle")
else:
    print("Scalene triangle") # all different side 