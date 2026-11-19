"""Module 10 – List Comprehensions
Run one example at a time. Examples progress from Easy to Hard.
"""

# Easy 1: Create numbers
numbers = [x for x in range(1, 6)]
print(numbers)


# Easy 2: Create squares
squares = [x ** 2 for x in range(1, 6)]
print(squares)


# Easy 3: Double each number
values = [2, 4, 6]
doubled = [x * 2 for x in values]
print(doubled)


# Easy 4: Convert words to uppercase
words = ["python", "list", "code"]
upper_words = [word.upper() for word in words]
print(upper_words)


# Intermediate 1: Filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens)


# Intermediate 2: Keep passing grades
grades = [72, 85, 90, 68, 77]
passed = [grade for grade in grades if grade >= 75]
print(passed)


# Intermediate 3: First letters
names = ["Ana", "Ben", "Carlo"]
initials = [name[0] for name in names]
print(initials)


# Hard: Process scores with conditions
scores = [65, 74, 80, 91, 100]
curved = [min(score + 5, 100) for score in scores]
remarks = ["Passed" if score >= 75 else "Failed" for score in curved]
high_scores = [score for score in curved if score >= 90]
print("Curved:", curved)
print("Remarks:", remarks)
print("90 and above:", high_scores)


