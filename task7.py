#Print numbers from 1 to 10

for i in range(1, 11):
    print(i)


#Display multiplication table for a given number

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


#Find factorial of a number

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial :", factorial)


#Generate the first N Fibonacci numbers

n = int(input("Enter N: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print()


#Check if a number is prime

num = int(input("Enter a number: "))
prime = True

if num < 2:
    prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

if prime:
    print("Prime number")
else:
    print("Not prime number")


#Reverse a number (e.g., 123 -> 321)

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number :", reverse)


#Count digits in a number

num = int(input("Enter a number: "))

count = 0

if num == 0:
    count = 1
else:
    while num != 0:
        num = num // 10
        count = count + 1

print("Number of digits :", count)


#Find sum of even numbers between 1-100

sum_even = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum_even = sum_even + i

print("Sum of even numbers (between 1-10): ", sum_even)


#Print a pyramid pattern

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    
    #spaces
    for j in range(rows - i):
        print(" ", end="")
    
    #stars
    for j in range(2 * i - 1):
        print("*", end="")
    
    print()


#Find all divisors of a number

num = int(input("Enter a number: "))

print("Divisors are: ")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)