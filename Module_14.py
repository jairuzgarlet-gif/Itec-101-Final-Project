"""Module 14 – File Streaming
Run one example at a time. Examples progress from Easy to Hard.
"""

# Easy 1: Write a text file
with open("message.txt", "w", encoding="utf-8") as file:
    file.write("Hello from Python!")


# Easy 2: Read a text file
with open("message.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)


# Easy 3: Add another line
with open("message.txt", "a", encoding="utf-8") as file:
    file.write("\nThis is a new line.")


# Easy 4: Read line by line
with open("message.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


# Intermediate 1: Save a list of names
names = ["Ana", "Ben", "Carlo"]
with open("names.txt", "w", encoding="utf-8") as file:
    for name in names:
        file.write(name + "\n")


# Intermediate 2: Count file lines
with open("names.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
print("Number of names:", len(lines))


# Intermediate 3: Handle a missing file
try:
    with open("notes.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist yet.")


# Hard: Simple notes app
filename = "my_notes.txt"
note = input("Write a note: ")
with open(filename, "a", encoding="utf-8") as file:
    file.write(note + "\n")
print("\nSaved notes:")
with open(filename, "r", encoding="utf-8") as file:
    print(file.read())


