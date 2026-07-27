# ==========================================
# Day 14 (Repeat)
# Module 3 - Raise, Assert & Validation
# ==========================================

print("===== Raise and Validation Practice =====")


# ------------------------------------------
# Example 1 - Age Validation
# ------------------------------------------

print("\nExample 1")

try:

    age = int(input("Enter your age: "))

    if age < 0:

        raise ValueError("Age cannot be negative.")

    print("Age Accepted")

except ValueError as error:

    print(error)


# ------------------------------------------
# Example 2 - Marks Validation
# ------------------------------------------

print("\nExample 2")

try:

    marks = int(input("Enter your marks: "))

    if marks < 0 or marks > 100:

        raise ValueError("Marks should be between 0 and 100.")

    print("Marks Saved")

except ValueError as error:

    print(error)


# ------------------------------------------
# Example 3 - Password Validation
# ------------------------------------------

print("\nExample 3")

password = input("Create password: ")

if len(password) < 8:

    print("Password is too short.")

else:

    print("Password Accepted")


# ------------------------------------------
# Example 4 - Email Validation
# ------------------------------------------

print("\nExample 4")

email = input("Enter your email: ")

if "@" in email:

    print("Valid Email")

else:

    print("Invalid Email")


# ------------------------------------------
# Example 5 - ATM Balance Check
# ------------------------------------------

print("\nExample 5")

try:

    balance = 5000

    amount = int(input("Enter withdraw amount: "))

    if amount > balance:

        raise ValueError("Insufficient Balance")

    print("Transaction Successful")

    print("Remaining Balance =", balance - amount)

except ValueError as error:

    print(error)


# ------------------------------------------
# Example 6 - Assert Example
# ------------------------------------------

print("\nExample 6")

try:

    number = int(input("Enter a positive number: "))

    assert number > 0, "Number must be greater than zero."

    print("Good Job!")

except AssertionError as error:

    print(error)

except ValueError:

    print("Please enter numbers only.")


print("\nModule 3 Practice Completed.")