

# ACCESS: https://chatgpt.com/share/c4da1dca-6eef-4f98-968f-b9a06d37f573
# Python Examples with Full Explanations

# 1. Variables and Type Casting
# Variables are used to store data. They allow you to keep track of information throughout your program.
# A variable can hold data of various types, such as strings, integers, floats, and booleans.

name = "Alice"  # String type
age = 25        # Integer type
pi = 3.14159    # Float type
is_student = True  # Boolean type

# Printing the values stored in the variables
print(f"Name: {name}, Age: {age}, Pi: {pi}, Is Student: {is_student}")

# Type casting is converting one data type to another.
# For example, you can convert a float to an integer or a string to an integer.

# Convert float to integer (note that this truncates the decimal part)
print(int(pi))  # Outputs: 3

# Convert string to integer (if the string contains a number)
num_str = "100"
num_int = int(num_str)
print(f"String '{num_str}' converted to integer: {num_int}")

# 2. User Input
# The input() function is used to get input from the user. The input is always returned as a string.

user_name = input("Enter your name: ")  # Prompts the user to enter their name
print(f"Hello, {user_name}!")

# To get an integer from the user, you must convert the input string to an integer using int().

user_age = int(input("Enter your age: "))  # Takes user input and converts it to an integer
print(f"Next year, you will be {user_age + 1} years old.")

# 3. Arithmetic and Math
# Python supports all basic arithmetic operations like addition, subtraction, multiplication, and division.

sum_value = 5 + 3       # Addition
difference = 10 - 4     # Subtraction
product = 7 * 6         # Multiplication
quotient = 8 / 2        # Division (returns a float)
integer_division = 8 // 3  # Integer (floor) division (returns an integer)
remainder = 10 % 3      # Modulus (remainder after division)
exponent = 2 ** 3       # Exponentiation (2 raised to the power of 3)

print(f"Sum: {sum_value}, Difference: {difference}, Product: {product}, Quotient: {quotient}")
print(f"Integer Division: {integer_division}, Remainder: {remainder}, Exponent: {exponent}")

# The math module provides additional mathematical functions.

import math

sqrt_16 = math.sqrt(16)  # Square root of 16
print(f"Square root of 16: {sqrt_16}")

# 4. If Statement
# Conditional statements allow you to run different code based on certain conditions.

number = 10
if number > 5:
    print("The number is greater than 5.")
elif number == 5:
    print("The number is equal to 5.")
else:
    print("The number is less than 5.")

# You can combine conditions using logical operators (and, or, not).

age = 20
if age > 18 and age < 30:
    print("You are in your 20s!")

# 5. Logical Operators
# Logical operators are used to combine multiple conditions.

x = True
y = False

# and operator (returns True only if both conditions are True)
print(f"x and y: {x and y}")  # Outputs: False

# or operator (returns True if at least one condition is True)
print(f"x or y: {x or y}")    # Outputs: True

# not operator (reverses the logical state)
print(f"not x: {not x}")      # Outputs: False

# 6. String Methods
# Python provides several methods to manipulate strings.

my_string = "hello world"

# Convert to uppercase
print(my_string.upper())

# Capitalize the first letter
print(my_string.capitalize())

# Replace a substring with another string
print(my_string.replace("world", "Python"))

# Find the index of a substring
print(my_string.find("world"))  # Outputs: 6

# Split the string into a list of words
print(my_string.split())  # Outputs: ['hello', 'world']

# 7. Format Specifiers
# Format specifiers allow you to format strings, numbers, and other data types for output.

temperature = 23.456
# Format the temperature to show only two decimal places
print(f"Temperature: {temperature:.2f}")  # Outputs: Temperature: 23.46

# You can also format integers with leading zeros.
number = 7
print(f"Number: {number:03}")  # Outputs: Number: 007

# 8. While Loop
# A while loop repeats a block of code as long as a condition is True.

counter = 0
while counter < 5:
    print(counter)
    counter += 1  # Increment the counter to avoid an infinite loop

# 9. For Loop
# A for loop is used to iterate over a sequence (like a list, string, or range of numbers).

for i in range(5):
    print(f"Number: {i}")

# You can also iterate over elements of a list or string.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 10. Lists, Tuples, Sets
# Lists are mutable (can be changed), tuples are immutable (cannot be changed), and sets are unordered collections of unique items.

my_list = [1, 2, 3, 4, 5]  # List
my_tuple = (10, 20, 30)    # Tuple
my_set = {1, 2, 3, 4, 5}   # Set

my_list.append(6)  # Adds an element to the list
print(f"List: {my_list}, Tuple: {my_tuple}, Set: {my_set}")

# Tuples are immutable, so you cannot change their elements.
# Sets do not allow duplicate values.

# 11. 2D Collections
# A 2D collection (like a list of lists) can represent a matrix or grid.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    print(row)

# 12. Dictionaries
# Dictionaries store data in key-value pairs.

person = {"name": "Alice", "age": 25}
print(f"Name: {person['name']}, Age: {person['age']}")

# You can add new key-value pairs or update existing ones.
person["city"] = "New York"
print(person)

# 13. Random Numbers
import random
# Generate a random integer between 1 and 10
random_number = random.randint(1, 10)
print(f"Random number: {random_number}")

# You can also shuffle a list randomly.
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")

# 14. Functions
# Functions allow you to define reusable blocks of code.

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Functions can take multiple arguments.
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 3))

# Functions can return multiple values.
def swap(a, b):
    return b, a

x, y = swap(10, 20)
print(f"Swapped: x = {x}, y = {y}")

# 15. Iterables
# An iterable is any object that can return its elements one at a time, such as a list, tuple, or string.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Strings are also iterables.
for char in "hello":
    print(char)

# 16. Membership Operators
# Membership operators check whether a value is present in a sequence (such as a list, tuple, or string).

fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # Outputs: True
print("grape" not in fruits)  # Outputs: True


# 17. Match-Case Statements (Python 3.10+)
# Match-case is similar to switch-case statements found in other languages.
# It allows you to match a value or pattern and execute the corresponding block of code.

def classify_number(x):
    match x:
        case 1:
            return "One"
        case 2:
            return "Two"
        case _:
            return "Unknown number"
print(classify_number(1))  # Outputs: One

# 18. Modules (datetime example)
# Modules are Python files that contain definitions and statements.
# You can import built-in or user-defined modules to reuse code.

import datetime
# The datetime module provides classes to manipulate dates and times.
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Outputs the current date and time

# 19. Scope Resolution (LEGB rule)
# Python uses the LEGB rule (Local, Enclosing, Global, Built-in) to resolve variable names.
x = "global"

def outer():
    x = "enclosing"
    def inner():
        nonlocal x  # Refers to the 'enclosing' variable
        x = "local"
        print(x)  # Outputs: local
    inner()
    print(x)  # Outputs: local (modified by nonlocal)
outer()

# 20. Object-Oriented Programming (OOP)
# OOP allows you to structure your code by creating objects that represent real-world entities.
# A class is a blueprint for objects, and objects are instances of classes.

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog("Buddy")
print(dog.speak())  # Outputs: Woof!

# 21. Super Method
# The super() function allows you to call a method from the parent class in a subclass.

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, position):
        super().__init__(name)  # Call the parent class's constructor
        self.position = position

emp = Employee("Alice", "Developer")
print(emp.name, emp.position)  # Outputs: Alice Developer

# 22. Static Methods
# Static methods are methods that belong to the class rather than any specific instance.

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

print(MathOperations.add(5, 10))  # Outputs: 15

# 23. Magic Methods
# Magic methods are special methods in Python that begin and end with double underscores.
# They allow you to define custom behavior for basic operators and functions.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Custom behavior for the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Calls the __add__ method
print(f"Point: ({p3.x}, {p3.y})")  # Outputs: Point: (4, 6)

# 24. Property
# The property decorator allows you to define getters and setters for attributes in a class.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

circle = Circle(5)
print(circle.radius, circle.area)  # Outputs: 5 78.53975

# 25. Decorators
# A decorator is a function that modifies the behavior of another function.
# Decorators are often used to add functionality to existing code.

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()  # Outputs: Before function call, Hello!, After function call

# 26. Exception Handling
# Exception handling allows you to handle errors gracefully and prevent the program from crashing.

try:
    x = 1 / 0  # Division by zero raises an exception
except ZeroDivisionError:
    print("You can't divide by zero!")  # Outputs: You can't divide by zero!

# 27. File Detection
# The os module provides functions to interact with the operating system, such as detecting files.

import os
if os.path.exists("example.txt"):
    print("File exists.")
else:
    print("File does not exist.")

# 28. Dates and Times
# The datetime module allows you to work with dates and times in Python.

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Outputs: current date and time

# 29. Multithreading
# Multithreading allows you to run multiple tasks concurrently.

import threading
import time

def thread_task():
    for i in range(3):
        print(f"Task {i}")
        time.sleep(1)

t1 = threading.Thread(target=thread_task)
t1.start()
t1.join()  # Waits for the thread to complete

# 30. Request API Data
# APIs (Application Programming Interfaces) allow you to interact with external systems and retrieve or send data.
# You can make HTTP requests to APIs using the requests module.

import requests

# Making a GET request to retrieve data from a sample API
response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(data[0])  # Print the first post
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

# Making a POST request to send data to an API
url = "https://jsonplaceholder.typicode.com/posts"
post_data = {
    "title": "New Post",
    "body": "This is a new post created using the API.",
    "userId": 1
}
response = requests.post(url, json=post_data)

if response.status_code == 201:  # 201 Created
    print("Post created successfully!", response.json())
else:
    print(f"Failed to create post. Status code: {response.status_code}")



