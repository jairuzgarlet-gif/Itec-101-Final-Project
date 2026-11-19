"""Module 3 – if/elif/else & Nested ifs
Run one example at a time. Examples progress from Easy to Hard.
"""

# Easy 1: Classify a number
number = 6
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Easy 2: Grade remark
grade = 88
if grade >= 90:
    print("Excellent")
elif grade >= 75:
    print("Passed")
else:
    print("Failed")


# Easy 3: Day category
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")


# Easy 4: Temperature label
temperature = 29
if temperature >= 35:
    print("Hot")
elif temperature >= 25:
    print("Warm")
else:
    print("Cool")


# Intermediate 1: Letter grade
score = int(input("Score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 75:
    print("C")
else:
    print("Needs improvement")


# Intermediate 2: Nested login check
username = input("Username: ")
password = input("Password: ")
if username == "student":
    if password == "python123":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Unknown username")


# Intermediate 3: Shipping fee
amount = float(input("Order amount: "))
member = input("Member? (yes/no): ").lower()
if member == "yes":
    if amount >= 500:
        fee = 0
    else:
        fee = 40
elif amount >= 1000:
    fee = 0
else:
    fee = 80
print("Shipping fee:", fee)


# Hard: Simple admission checker
age = int(input("Age: "))
score = float(input("Entrance score: "))
if age >= 15:
    if score >= 85:
        print("Qualified")
    elif score >= 75:
        print("For interview")
    else:
        print("Score requirement not met")
else:
    print("Age requirement not met")


