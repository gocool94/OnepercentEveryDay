1. **Class and Objects:**
   - Implement a class for a simple bank account with methods for deposit, withdraw, and checking balance.
   - Create a class hierarchy for different types of vehicles (car, bike, truck) with shared and specific attributes/methods.

---

\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\*** i n t e r v i e w \***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\*** q u e s t i o n s **\*\***\*\*\*\***\*\***\*\***\*\***\*\*\*\***\*\***

1.  **Explain the key principles of object-oriented programming (OOP).**
    The main concept of OOPs is to bind the data and the functions
    that work on that together as a single unit so that no other part of the code can access this data.
    concepts of OOPS are inheritance,polymorphism,encapsulation
2.  **What is a class in Python, and how do you define a class?**
    1. Class is a collection of objects, that contains the prototype to which an object is created
    2. It is a logical entity of attributes and methods
3.  **Explain the difference between a class and an object in Python.**
    1. Class - Its a blueprint that contains how the objects are going to be created
    2. object - its a instance of a class that allows to use the method and attributes inside the class
4.  **What are instance variables and class variables? How do they differ?**

    1. Instance variable - Instance variable are defined when the instance of a class is being created
       Example:
       //
       class CoffeeOrder:
       def **init**(self, coffee_name, price):
       self.coffee_name = coffee_name
       self.price = price
       //

       class variable -> these variables are creted when the class is being created
       Example:
       //
       class Vehicle:
       number_of_tyres = 2
       //

5.  **Discuss the concept of encapsulation in object-oriented programming.**

    - Encapsulation is binding up of data and methods together
    - we can hide the objects internal representation from outside which is data hiding

    private members are with "\_" and "\_\_" in the prefix

                   class Employee:
                      # constructor
                      def __init__(self, name, salary):
                         # public data member
                         self.name = name
                         # private member
                         self.__salary = salary

                   # creating object of a class
                   emp = Employee('Jessa', 10000)

                   print('Name:', emp.name)
                   # direct access to private member using name mangling
                   print('Salary:', emp._Employee__salary)

6.  **Explain the significance of constructors (`__init__` method) in Python classes.**

         "__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.



         ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

7.  **Inheritance and Polymorphism:**

"""Inheritance is the capability of one class to derive or inherit the properties from another class. The class that derives properties is called the derived class or child class and the class from which the properties are being derived is called the base class or parent class. """

    - Create a base class `Shape` with subclasses `Circle` and `Rectangle`. Implement methods to calculate area for each shape.

    - Design a class structure for a library system with `Person`, `Author`, and `Book` classes using inheritance.

\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\*** i n t e r v i e w \***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\*** q u e s t i o n s **\*\***\*\*\*\***\*\***\*\***\*\***\*\*\*\***\*\***

7.  **What is inheritance in Python, and how is it implemented? Provide an example.**

    1. Its a OOPS concept for resuability where the Base class or the parent class is used as a reference/
       copy to derive another class with another need.

       class Person:
       def **init**(self, name, age):
       self.name = name
       self.age = age

    def display_info(self):
    print(f"Name: {self.name}, Age: {self.age}")

class Author(Person):
def **init**(self, name, age, genre):
super().**init**(name, age)
self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")

class Book:
def **init**(self, title, author, year):
self.title = title
self.author = author
self.year = year

    def display_info(self):
        print(f"Title: {self.title}")
        self.author.display_info()
        print(f"Year: {self.year}")

# Creating instances

author1 = Author("Jane Doe", 40, "Mystery")
book1 = Book("The Secret Garden", author1, 1911)

# Displaying information

book1.display_info()

8.  **Explain the difference between single inheritance and multiple inheritance in Python.**

single :
class Parent:
pass

class Child(Parent):
pass

Multiple:
class Parent1:
pass

class Parent2:
pass

class Child(Parent1, Parent2):
pass

Multi level:
class Grandparent:
pass

class Parent(Grandparent):
pass

class Child(Parent):
pass

         ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

9.  **Encapsulation:**

    - Implement a `Student` class with private attributes for name, age, and grade. Provide methods to access and modify these attributes.
    - Create a class for a `BankAccount` with a private attribute for balance and methods for deposit and withdrawal.

\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\*** i n t e r v i e w \***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\*** q u e s t i o n s **\*\***\*\*\*\***\*\***\*\***\*\***\*\*\*\***\*\***

How do you access private attributes outside the class?

Private attributes can be accessed using name mangling. For example, if an attribute named **attribute exists in a class MyClass, it can be accessed outside the class using \_MyClass**attribute.

---

1.  **Abstraction:**

    - Implement an abstract class `Animal` with subclasses `Dog` and `Cat`. Define common and specific methods for each subclass.
    - Design an abstract class `Shape` with subclasses for different shapes. Implement a method to calculate perimeter in each subclass.

2.  **Method Overriding and Overloading:**

- Create a base class `Person` with a method `introduce`. Create subclasses `Student` and `Teacher` that override the `introduce` method.
- Implement a class `Calculator` with methods for addition, subtraction, and multiplication. Use method overloading to support different argument types.

11. **Composition and Aggregation:**

- Create a class `Department` with a list of `Employee` objects as an attribute to represent employee aggregation.
- Implement a class `Car` with a composition relationship to `Engine` and `Wheel` objects.

12. **Interfaces and Abstract Methods:**

- Define an interface `Shape` with an abstract method `calculate_area`. Implement this interface in classes like `Circle` and `Rectangle`.
- Create an abstract class `Transport` with methods for `start`, `stop`, and `accelerate`. Implement this in classes like `Car` and `Bike`.

13. **Static and Class Methods:**

- Implement a class `Math` with static methods for common mathematical operations (addition, subtraction, etc.).
- Create a class `Employee` with a class method to calculate the average salary of all employees.

14. **Operator Overloading:**

- Overload the `+` operator for a class `Vector` to perform vector addition.
- Implement custom comparison methods to compare two objects of a class based on a specific attribute.

15. **Design Patterns:**

    - Implement the Singleton pattern for a class `Logger` to ensure only one instance is created.
    - Use the Factory Method pattern to create different types of `Product` objects based on a given input.

16. **Dependency Injection:**

    - Create a class `EmailSender` that takes an instance of `Logger` as a dependency to log emails sent.
    - Implement a class `PaymentProcessor` that accepts a payment gateway as a parameter to process payments.

17. **Composition Over Inheritance:**

    - Design a class structure for a drawing application using composition to create complex shapes.
    - Create a class `Animal` and a class `Sound` that can be composed to represent the sound an animal makes.

18. **Duck Typing and Polymorphism:**

    - Implement a function that accepts any object with a `speak` method and calls it to produce a sound.
    - Create a generic class `Container` that accepts and manages any type of objects.

19. **Method Chaining:**

    - Implement a class `StringBuilder` with methods to append, reverse, and get the final string. Enable method chaining.
    - Design a class `Query` with methods to add conditions, select columns, and execute the query. Enable method chaining.

20. **Data Hiding and Encapsulation:**
    - Create a class `Person` with private attributes for name and age, and methods to access and update them.
    - Implement a class `BankAccount` with a private attribute for balance and methods to deposit and withdraw money.
