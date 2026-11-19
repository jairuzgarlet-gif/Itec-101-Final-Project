"""Module 6 – for-in range Loops
Run one example at a time. Examples progress from Easy to Hard.
"""

# Easy 1: Print 0 to 4
for number in range(5):
    print(number)


# Easy 2: Print 1 to 5
for number in range(1, 6):
    print(number)


# Easy 3: Even numbers
for number in range(2, 11, 2):
    print(number)


# Easy 4: Countdown
for number in range(5, 0, -1):
    print(number)


# Intermediate 1: Sum from 1 to n
n = int(input("Enter n: "))
total = 0
for number in range(1, n + 1):
    total += number
print("Sum:", total)


# Intermediate 2: Multiplication table
n = int(input("Number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# Intermediate 3: Count vowels in a word
word = input("Word: ").lower()
count = 0
for letter in word:
    if letter in "aeiou":
        count += 1
print("Vowels:", count)


# Hard: Average of entered scores
scores = []
for i in range(5):
    score = float(input(f"Score {i + 1}: "))
    scores.append(score)
average = sum(scores) / len(scores)
print("Scores:", scores)
print("Average:", average)


