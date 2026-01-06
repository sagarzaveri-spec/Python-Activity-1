'''
class A:
    pass
class B(A): #A is the parent class and B is the base class. 
'''

'''
class dad:
    def __init__(self,eyes,aggression):
        self.eyes=eyes
        self.aggression=aggression
    def display(self):
        print("Your eye colour is",self.eyes)
        print("You are aggressive",self.aggression)

#Child Class
class son(dad):
    def __init__(self,name,age,eyes,aggression):
        self.name=name
        self.age=age
        #dad.__init__(self,eyes,aggression)
        super().__init__(eyes,aggression)
    def display_information(self):
        print("The son's name is",self.name)
        print("The sons' age is",self.age)

#Object Creation
object=son("Penguin",22,"Brown",True)

object.display_information()
object.display()
'''

class Employees:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_information(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
class Teacher(Employees):
    def __init__(self,name,salary,subject):
        super().__init__(name,salary)
        self.subject=subject
    def display_information(self):
        super().display_information()
        print(f"Subject: {self.subject}")
class Developer(Employees):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language=language
    def display_information(self):
        super().display_information()
        print(f"Language: {self.language}")
Professor=Teacher("Ashrafi",667893,"Coding")
Software_Developer=Developer('Sagar',223124,'English')
print("Teacher Details:")
Professor.display_information()
print("Developer Details: ")
Software_Developer.display_information()

#import necessary packages
from abc import ABC, abstractmethod
#create a base class
class Animal(ABC):
    #abstract method
    #should be implemented y all sub-classes
    def move(self):
        pass
#Sub classes
class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can bark")

class Lion(Animal):
    def move(self):
        print("I can roar")

#Driver code
R=Human()
R.move()
K=Snake()
K.move()
D=Dog()
D.move()
L=Lion()
L.move()