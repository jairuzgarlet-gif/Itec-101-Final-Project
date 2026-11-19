"""Module 9 – List Methods vs Functions
Run one example at a time. Examples progress from Easy to Hard.
"""

# Easy 1: len() function
names = ["Mia", "Leo", "Kai"]
print(len(names))


# Easy 2: append() method
numbers = [1, 2]
numbers.append(3)
print(numbers)


# Easy 3: sum() function
scores = [80, 90, 85]
print(sum(scores))


# Easy 4: sort() method
values = [4, 1, 3, 2]
values.sort()
print(values)


# Intermediate 1: sorted() function
values = [4, 1, 3, 2]
new_values = sorted(values)
print("Original:", values)
print("Sorted copy:", new_values)


# Intermediate 2: remove() and pop()
colors = ["red", "blue", "green"]
colors.remove("blue")
last_color = colors.pop()
print(colors)
print("Removed:", last_color)


# Intermediate 3: min(), max(), and sum()
temperatures = [28, 31, 27, 30]
print("Lowest:", min(temperatures))
print("Highest:", max(temperatures))
print("Total:", sum(temperatures))


# Hard: Analyze quiz scores
scores = [78, 92, 85, 92, 69]
print("Count:", len(scores))
print("Average:", sum(scores) / len(scores))
print("Highest:", max(scores))
print("Lowest:", min(scores))
print("Descending:", sorted(scores, reverse=True))
print("Number of 92s:", scores.count(92))


