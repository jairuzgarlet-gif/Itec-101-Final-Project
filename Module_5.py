"""Module 5 – while Loops
Run one example at a time. Examples progress from Easy to Hard.
"""

# Easy 1: Count from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1


# Easy 2: Count down
number = 5
while number > 0:
    print(number)
    number -= 1
print("Go!")


# Easy 3: Repeat a message
count = 0
while count < 3:
    print("Keep learning!")
    count += 1


# Easy 4: Sum numbers
number = 1
total = 0
while number <= 5:
    total += number
    number += 1
print("Total:", total)


# Intermediate 1: Password attempts
password = ""
while password != "python":
    password = input("Enter password: ")
print("Access granted")


# Intermediate 2: Input until zero
total = 0
value = int(input("Enter a number (0 to stop): "))
while value != 0:
    total += value
    value = int(input("Enter a number (0 to stop): "))
print("Sum:", total)


# Intermediate 3: Multiplication table
n = int(input("Number: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1


# Hard: Menu-driven wallet
balance = 500
choice = ""
while choice != "3":
    print("\n1. View balance  2. Add money  3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        print("Balance:", balance)
    elif choice == "2":
        amount = float(input("Amount to add: "))
        if amount > 0:
            balance += amount
        print("Updated balance:", balance)
    elif choice == "3":
        print("Goodbye")
    else:
        print("Invalid choice")


