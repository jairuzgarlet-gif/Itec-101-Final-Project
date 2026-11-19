"""Module 11 – Functions
Run one example at a time. Examples progress from Easy to Hard.
"""

# Easy 1: Define a greeting
def greet():
    print("Hello!")

greet()


# Easy 2: Function with a parameter
def greet_user(name):
    print("Welcome,", name)

greet_user("Alex")


# Easy 3: Return a sum
def add(a, b):
    return a + b

print(add(5, 3))


# Easy 4: Default parameter
def introduce(name, country="Philippines"):
    print(name, "is from", country)

introduce("Mika")
introduce("Sam", "Japan")


# Intermediate 1: Check even number
def is_even(number):
    return number % 2 == 0

print(is_even(8))
print(is_even(5))


# Intermediate 2: Calculate average
def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(average([80, 90, 85]))


# Intermediate 3: Convert minutes
def convert_minutes(minutes):
    hours = minutes // 60
    remaining = minutes % 60
    return hours, remaining

h, m = convert_minutes(135)
print(h, "hours and", m, "minutes")


# Hard: Student grade report
def get_remark(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Passed"
    return "Failed"

def print_report(name, scores):
    mean = sum(scores) / len(scores)
    print("Student:", name)
    print("Average:", round(mean, 2))
    print("Remark:", get_remark(mean))

print_report("Alex", [88, 92, 85])


