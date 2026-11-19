# EASY 1: Create and display a tuple
colors = ("red", "blue", "green")
print(colors)


# EASY 2: Access tuple items
subjects = ("Math", "Science", "English")
print("First subject:", subjects[0])
print("Last subject:", subjects[-1])


# EASY 3: Create a set with repeated values
numbers = {1, 2, 2, 3, 3, 4}
print("Unique numbers:", numbers)


# EASY 4: Create and access a dictionary
student = {
    "name": "Alex",
    "age": 16,
    "section": "STEM"
}
print("Name:", student["name"])
print("Age:", student["age"])


# INTERMEDIATE 1: Count items in a tuple
votes = ("A", "B", "A", "C", "A", "B")

print("Votes for A:", votes.count("A"))
print("Position of C:", votes.index("C"))


# INTERMEDIATE 2: Set operations
science_club = {"Ana", "Ben", "Carlo"}
math_club = {"Ben", "Dina", "Carlo"}

print("Members in both clubs:", science_club & math_club)
print("All club members:", science_club | math_club)
print("Only in science club:", science_club - math_club)


# INTERMEDIATE 3: Update a dictionary
inventory = {
    "notebook": 10,
    "pencil": 20
}

inventory["eraser"] = 8
inventory["pencil"] += 5
inventory.pop("notebook")

print("Updated inventory:", inventory)


# HARD: Student Records System
students = {
    "S001": {"name": "Ana", "scores": [90, 85, 92]},
    "S002": {"name": "Ben", "scores": [78, 88, 80]},
    "S003": {"name": "Carlo", "scores": [95, 91, 89]}
}

for student_id, details in students.items():
    average = sum(details["scores"]) / len(details["scores"])

    print(f"\n{student_id} - {details['name']}")
    print("Average:", round(average, 2))

    if average >= 90:
        print("Remark: Excellent")
    elif average >= 75:
        print("Remark: Passed")
    else:
        print("Remark: Failed")