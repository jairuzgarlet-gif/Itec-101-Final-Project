"""Module 1 – Printing, Input & Variables
Run one example at a time. Examples progress from Easy to Hard.
"""

# Easy 1: Print a message
print("Hello, Python!")


# Easy 2: Print multiple lines
print("Name: Alex")
print("Section: STEM")


# Easy 3: Store a name
name = "Alex"
print(name)


# Easy 4: Store different data types
name = "Alex"
age = 16
height = 1.65
is_student = True
print(name, age, height, is_student)


# Intermediate 1: Ask for a name
name = input("Enter your name: ")
print("Welcome,", name)


# Intermediate 2: Convert input to integer
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)


# Intermediate 3: Calculate a rectangle
length = float(input("Length: "))
width = float(input("Width: "))
area = length * width
print("Area:", area)


# Hard: Simple student profile
name = input("Student name: ")
section = input("Section: ")
age = int(input("Age: "))
print("\nSTUDENT PROFILE")
print(f"{name} | {section} | {age} years old")


