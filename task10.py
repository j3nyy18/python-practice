#basic structure
"""
class ClassName:
    def __init__(self, data):
        self.data = data

object1 = ClassName(value)
object1.method()
"""

#Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.

class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print("Speed after acceleration: ", self.speed)

    def brake(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0
        print("Speed after braking: ", self.speed)

car = Car("Toyota", "Camry", 50)

print("Car: ", car.brand, car.model)
print("Initial speed:", car.speed)

car.accelerate()
car.brake()


#Create a BankAccount class with deposit and withdraw methods.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited: ", amount)
        print("Current balance: ", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn: ", amount)
            print("Current balance: ", self.balance)
        else:
            print("Insufficient balance!")

account = BankAccount("Jeny", 10000)

print("Account Holder: ", account.account_holder)
print("Initial Balance: ", account.balance)

account.deposit(2000)
account.withdraw(3000)


#Create a Student class with a method to calculate average marks.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        average = sum(self.marks) / len(self.marks)
        return average

student = Student("Jeny", [85, 90, 78, 92, 88])

print("Student: ", student.name)
print("Marks: ", student.marks)
print("Average marks: ", student.calculate_average())


#Create a Rectangle class with methods to find area and perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle = Rectangle(10, 5)

print("Rectangle Area: ", rectangle.area())
print("Rectangle Perimeter: ", rectangle.perimeter())

#Create an Employee class that displays salary details.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary_details(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

employee = Employee("Jeny", 30000)

print("Employee Details:")
employee.display_salary_details()


# 6. Create a Book class to store title, author, and price, and display details.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Price: ", self.price)

book = Book("Think like a monk", "Jay Shetty", 500)

print("Book Details:")
book.display_details()


#Create a Circle class to find area and circumference.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

circle = Circle(7)

print("Circle Area: ", circle.area())
print("Circle Circumference: ", circle.circumference())


#Create a Laptop class with a method to apply discounts on price.

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, discount_percentage):
        discount = self.price * discount_percentage / 100
        final_price = self.price - discount

        return final_price


laptop = Laptop("Dell", 60000)

print("Laptop Brand:", laptop.brand)
print("Original Price:", laptop.price)

final_price = laptop.apply_discount(10)

print("Price after 10% discount:", final_price)

#Create a Flight class with seat booking functionality.

class Flight:
    def __init__(self, flight_number, total_seats):
        self.flight_number = flight_number
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.total_seats:
            self.booked_seats += 1
            print("Seat booked successfully!")
            print("Available seats: ", self.total_seats - self.booked_seats)
        else:
            print("No seats available!")

flight = Flight("AI101", 3)

print("Flight Number:", flight.flight_number)

flight.book_seat()
flight.book_seat()
flight.book_seat()
flight.book_seat()


#Create a Shop class with a method to add and list products.

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(product, "added to shop!")

    def list_products(self):
        print("Products in shop: ")

        for product in self.products:
            print("-", product)

shop = Shop()

print("Shop Products: ")

shop.add_product("Laptop")
shop.add_product("Mouse")
shop.add_product("Keyboard")

shop.list_products()