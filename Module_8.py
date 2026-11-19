"""Module 8 – Lists of Lists & Nested Loops
Run one example at a time. Examples progress from Easy to Hard.
"""

# Easy 1: Create a 2D list
seats = [["A1", "A2"], ["B1", "B2"]]
print(seats)


# Easy 2: Access a nested item
grades = [[90, 85], [88, 92]]
print(grades[0][1])


# Easy 3: Print each row
grid = [[1, 2], [3, 4], [5, 6]]
for row in grid:
    print(row)


# Easy 4: Print every element
grid = [[1, 2], [3, 4]]
for row in grid:
    for value in row:
        print(value)


# Intermediate 1: Row totals
scores = [[80, 90], [75, 85], [88, 92]]
for row in scores:
    print("Row total:", sum(row))


# Intermediate 2: Count all passing grades
grades = [[80, 70], [95, 60], [88, 91]]
passed = 0
for row in grades:
    for grade in row:
        if grade >= 75:
            passed += 1
print("Passing grades:", passed)


# Intermediate 3: Display a multiplication grid
for row in range(1, 4):
    for column in range(1, 4):
        print(row * column, end="\t")
    print()


# Hard: Find the highest value in a matrix
matrix = [[4, 12, 7], [9, 3, 15], [6, 11, 2]]
highest = matrix[0][0]
position = (0, 0)
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] > highest:
            highest = matrix[r][c]
            position = (r, c)
print("Highest:", highest)
print("Row, column:", position)


