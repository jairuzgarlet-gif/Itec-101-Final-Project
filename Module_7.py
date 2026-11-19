"""Module 7 – List Basics & for-in
Run one example at a time. Examples progress from Easy to Hard.
"""

# Easy 1: Create and print a list
colors = ["red", "blue", "green"]
print(colors)


# Easy 2: Access an item
fruits = ["apple", "banana", "mango"]
print(fruits[0])
print(fruits[-1])


# Easy 3: Change an item
animals = ["cat", "dog", "bird"]
animals[1] = "rabbit"
print(animals)


# Easy 4: Loop through a list
subjects = ["Math", "Science", "Python"]
for subject in subjects:
    print(subject)


# Intermediate 1: Add and remove items
tasks = ["Read", "Study"]
tasks.append("Practice")
tasks.remove("Read")
print(tasks)


# Intermediate 2: Find the total
prices = [25, 40, 15, 20]
total = 0
for price in prices:
    total += price
print("Total:", total)


# Intermediate 3: Find the largest value
numbers = [12, 5, 30, 8, 21]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print("Largest:", largest)


# Hard: Simple attendance checker
students = ["Ana", "Ben", "Carlo", "Dina"]
present = ["Ana", "Carlo"]
for student in students:
    if student in present:
        print(student, "- Present")
    else:
        print(student, "- Absent")


