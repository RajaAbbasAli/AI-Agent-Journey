# Day 14 - Module 3
# raise and Input Validation

print("===== Module 3 Practice =====")

# -----------------------------
# Program 1
# Age Validation
# -----------------------------

print("\nProgram 1")

try:

    age = int(input("Enter Your Age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age Accepted")

except ValueError as error:

    print(error)

print("----------------------")


# -----------------------------
# Program 2
# Marks Validation
# -----------------------------

print("\nProgram 2")

try:

    marks = int(input("Enter Your Marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks should be between 0 and 100.")

    print("Marks Accepted")

except ValueError as error:

    print(error)

print("----------------------")


# -----------------------------
# Program 3
# Password Validation
# -----------------------------

print("\nProgram 3")

try:

    password = input("Enter Password: ")

    if len(password) < 8:
        raise ValueError("Password is too short.")

    print("Password Accepted")

except ValueError as error:

    print(error)

print("----------------------")


# -----------------------------
# Program 4
# Email Validation
# -----------------------------

print("\nProgram 4")

try:

    email = input("Enter Email: ")

    if "@" not in email:
        raise ValueError("Invalid Email.")

    print("Email Accepted")

except ValueError as error:

    print(error)

print("----------------------")


# -----------------------------
# Program 5
# ATM Balance Check
# -----------------------------

print("\nProgram 5")

balance = 10000

try:

    amount = int(input("Enter Amount: "))

    if amount > balance:
        raise ValueError("Insufficient Balance.")

    print("Transaction Successful")

except ValueError as error:

    print(error)

print("----------------------")

print("Module 3 Completed Successfully.")