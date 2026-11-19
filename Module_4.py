"""Module 4 – match/case (Switch)
Run one example at a time. Examples progress from Easy to Hard.
"""

# Easy 1: Match a number
day = 1
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Other day")


# Easy 2: Greeting choice
choice = "hello"
match choice:
    case "hello":
        print("Hi!")
    case "bye":
        print("Goodbye!")
    case _:
        print("Unknown command")


# Easy 3: Traffic light
light = "yellow"
match light:
    case "red": print("Stop")
    case "yellow": print("Prepare")
    case "green": print("Go")
    case _: print("Invalid color")


# Easy 4: Simple calculator choices
operator = "+"
match operator:
    case "+": print("Addition selected")
    case "-": print("Subtraction selected")
    case "*": print("Multiplication selected")
    case _: print("Unsupported operator")


# Intermediate 1: User menu
choice = input("Choose A, B, or C: ").upper()
match choice:
    case "A": print("Open profile")
    case "B": print("View grades")
    case "C": print("Exit menu")
    case _: print("Invalid choice")


# Intermediate 2: Month group
month = int(input("Month number: "))
match month:
    case 12 | 1 | 2: print("Cool season")
    case 3 | 4 | 5: print("Hot season")
    case 6 | 7 | 8 | 9 | 10 | 11: print("Rainy season")
    case _: print("Invalid month")


# Intermediate 3: Basic operation
a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Operator (+, -, *, /): ")
match op:
    case "+": result = a + b
    case "-": result = a - b
    case "*": result = a * b
    case "/" if b != 0: result = a / b
    case _: result = None
print("Result:", result if result is not None else "Invalid operation")


# Hard: Small help desk menu
choice = input("1-Password help, 2-Account help, 3-Exit: ")
match choice:
    case "1":
        topic = "password"
        print("Open the password reset guide.")
    case "2":
        topic = "account"
        print("Open the account support guide.")
    case "3":
        topic = "exit"
        print("Thank you.")
    case _:
        topic = "invalid"
        print("Please choose 1, 2, or 3.")


