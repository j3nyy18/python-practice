
"""
------------------Inheritance----------------

class Parent:
    def parent_method(self):
        pass

class Child(Parent):
    def child_method(self):
        pass

object1 = Child()
object1.parent_method()
object1.child_method()


-----------------Method Overriding---------------------

class Parent:
    def method(self):
        print("Parent method")

class Child(Parent):
    def method(self):
        print("Child method")

object1 = Child()
object1.method()


-----------------Multilevel Inheritance-----------------

class GrandParent:
    pass

class Parent(GrandParent):
    pass

class Child(Parent):
    pass

object1 = Child()


-----------------Multiple Inheritance-----------------

class Parent1:
    def method1(self):
        pass

class Parent2:
    def method2(self):
        pass

class Child(Parent1, Parent2):
    pass

object1 = Child()
object1.method1()
object1.method2()


-----------------Polymorphism-----------------

class Class1:
    def method(self):
        pass

class Class2:
    def method(self):
        pass

def function(object):
    object.method()


-----------------Encapsulation-----------------

class ClassName:
    def __init__(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data


-----------------------super()----------------------

class Parent:
    def __init__(self, data):
        self.data = data

class Child(Parent):
    def __init__(self, data, extra_data):
        super().__init__(data)
        self.extra_data = extra_data

object1 = Child(value1, value2)
"""

#Create a base class Animal and subclasses Dog and Cat.

class Animal:
    def speak(self):
        print("Animal makes a sound!")

class Dog(Animal):
    def bark(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def meow(self):
        print("Cat says: Meow!")

dog = Dog()
cat = Cat()

dog.speak()
dog.bark()

cat.speak()
cat.meow()


#Create a class hierarchy for Vehicle -> Car -> ElectricCar.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print("Brand: ", self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_car(self):
        print("Model: ", self.model)

class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def display_electric_car(self):
        print("Battery: ", self.battery, "kWh")


electric_car = ElectricCar("Tesla", "Model 3", 75)

print("Vehicle Details: ")
electric_car.display_brand()
electric_car.display_car()
electric_car.display_electric_car()


#Implement method overriding in a base and derived class.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog says: Woof!")

animal = Animal()
dog = Dog()

print("Method Overriding: ")
animal.sound()
dog.sound()


#Demonstrate multiple inheritance with two parent classes.

class Father:
    def father_skill(self):
        print("Father: Driving")

class Mother:
    def mother_skill(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def child_skill(self):
        print("Child: Coding")

child = Child()

print("Multiple Inheritance: ")
child.father_skill()
child.mother_skill()
child.child_skill()


#Create a polymorphic function that works with different shapes.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def display_area(shape):
    print("Area: ", shape.area())

circle = Circle(5)
rectangle = Rectangle(10, 5)

print("Polymorphism: ")
display_area(circle)
display_area(rectangle)


#Create a Bank system with SavingsAccount and CurrentAccount classes.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print("Account Holder: ", self.account_holder)
        print("Balance: ", self.balance)

class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print("Interest added:", interest)

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        self.balance -= amount
        print("Withdrawn: ", amount)


savings = SavingsAccount("Jeny", 10000)
current = CurrentAccount("Reny", 20000)

print("Savings Account: ")
savings.display_balance()
savings.add_interest(5)
savings.display_balance()

print("Current Account: ")
current.display_balance()
current.withdraw(5000)
current.display_balance()

#Create a class with private attributes and getter/setter methods.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative!")


person = Person("Jeny", 22)

print("Encapsulation: ")
print("Age: ", person.get_age())

person.set_age(23)

print("Updated age: ", person.get_age())


#Create a Teacher and Student class to show inheritance.

class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name: ", self.name)


class Teacher(Person):
    def teach(self):
        print(self.name, "is teaching!")


class Student(Person):
    def study(self):
        print(self.name, "is studying!")

teacher = Teacher("Mr. Patel")
student = Student("Jeny")

print("Teacher: ")
teacher.display_name()
teacher.teach()

print("Student: ")
student.display_name()
student.study()

#Create a MusicPlayer class and subclass Spotify to override play method.

class MusicPlayer:
    def play(self):
        print("Playing music.")

class Spotify(MusicPlayer):
    def play(self):
        print("Playing music from Spotify!")

player = MusicPlayer()
spotify = Spotify()

print("Music Player: ")
player.play()
spotify.play()


#Demonstrate the use of super() in inheritance.

class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display(self):
        super().display()
        print("Salary:", self.salary)

employee = Employee("Jeny", 30000)

print("super() Example:")
employee.display()
