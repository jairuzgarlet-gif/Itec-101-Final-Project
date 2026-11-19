"""Module 12 – String Methods
Run one example at a time. Examples progress from Easy to Hard.
"""

# Easy 1: Change letter case
message = "hello python"
print(message.upper())
print(message.lower())


# Easy 2: Title case
name = "jane dela cruz"
print(name.title())


# Easy 3: Remove extra spaces
text = "   welcome   "
print(text.strip())


# Easy 4: Count characters
word = "banana"
print("Length:", len(word))
print("a count:", word.count("a"))


# Intermediate 1: Replace a word
sentence = "I like Java"
updated = sentence.replace("Java", "Python")
print(updated)


# Intermediate 2: Split a sentence
sentence = "Python is easy to practice"
words = sentence.split()
print(words)


# Intermediate 3: Find a word
sentence = "Learning Python is useful"
position = sentence.find("Python")
print("Position:", position)


# Hard: Basic username cleaner
raw_name = input("Enter your name: ")
clean_name = raw_name.strip().title()
username = clean_name.replace(" ", "_").lower()
print("Display name:", clean_name)
print("Suggested username:", username)


