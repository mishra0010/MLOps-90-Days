# Basic Class and Objects in Python
class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def drive(self):
        print("Car is driving")

car1 = Car("BMW","Blach")
car2 = Car("Tesla","White")

print(car1.brand)
car2.drive()

# Encapsulation in Python -- Binding Data + Method together
class BankAccount:
    def __init__(self,balance):
        self.balace = balance
    def showBalance(self):
        print(self.balace)

# Inheritance In Python -- Reusing the code

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dos barks")

d = Dog()
d.speak()
d.bark()

# Polymorphism in python -- One name different forms

class Cat:
    def sound(self):
        print("Meow")
class Dog:
    def sound(self):
        print("Woff")

animals = [Cat(),Dog()]
for animal in animals:
    animal.sound()

# Abstraction in Python -- Hiding the complex part

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass
class Bike(Vehicle):
    def move(self):
        print("Bike is moving")

b = Bike()
b.move()


