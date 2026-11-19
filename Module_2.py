"""Module 2 – Operators & Basic if/else
Run one example at a time. Examples progress from Easy to Hard.
"""

# Easy 1: Addition
a = 8
b = 4
print(a + b)


# Easy 2: Remainder
number = 17
print(number % 5)


# Easy 3: Compare two values
print(10 > 7)
print(3 == 5)


# Easy 4: Check an age
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")


# Intermediate 1: Even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Intermediate 2: Positive or negative
number = float(input("Number: "))
if number >= 0:
    print("Non-negative")
else:
    print("Negative")


# Intermediate 3: Pass or fail
score = float(input("Score: "))
if score >= 75:
    print("Passed")
else:
    print("Failed")


# Hard: Discount calculator
total = float(input("Purchase total: "))
if total >= 1000:
    discount = total * 0.10
else:
    discount = 0
print("Discount:", discount)
print("Amount to pay:", total - discount)


