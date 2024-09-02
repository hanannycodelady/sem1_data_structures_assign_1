# class is a blueprint of creating an object .


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

        print (Person)


 # An object is an instance of a class 
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def description(self):
        return f"The {self.color} car has {self.mileage} miles."

blue_car = Car("blue", 20000)
red_car = Car("red", 30000)

print(blue_car.description())  
print(red_car.description())



# Construtor is a special method in Python that is automatically called when an object is created from a class.
# This is also used in making models in api 
# example 
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        return f"{self.year} {self.make} {self.model}"
        
car = Car("mercedes", "G-series", 2022)
print(car.info())  

#  Inheritance & Types:
# Inheritance allows a class to inherit attributes and methods from another class
# This can be single, multiple, or multilevel inheritance.

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("The dog barks.")

my_animal = Animal("cow")
my_dog = Dog("chiwawa")

my_animal.sound()  
my_dog.sound()

# Polymorphism
# Polymorphism is the ability of an object to take on multiple forms

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(10)
rectangle = Rectangle(23, 5)

print(circle.area())  
print(rectangle.area())  


# Abstract Classes
# Abstract classes cannot be instantiated directly

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

circle = Circle(10)
print(f"Area: {circle.area()}")       
print(f"Perimeter: {circle.perimeter()}")  

