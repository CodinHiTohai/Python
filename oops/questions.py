# Create a class Car with a method drive() that prints "Car is moving".
# Create an object of Car and call drive().

class Car:
    def drive(self):
        print("car is Moving")
c1=Car()
c1.drive()

# /create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
# Create an object and print the person’s name and age.

class Perosn:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Perosn("govind",22)
print(p1.name)
print(p1.age)


# reate a base class Animal with a method sound() that prints "Some sound".
# Create a derived class Dog that overrides sound() to print "Bark!".
# Create an object of Dog and call sound().

# Downlo
class Animal:
    def sound(self):
        print("some sound")
class Dog(Animal):
    def sound(self):
        print("bark")
d1=Dog()
d1.sound()