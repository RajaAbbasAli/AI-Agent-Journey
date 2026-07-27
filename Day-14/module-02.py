# ===============================
# Day 14 (Repeat)
# Module 2 - try, except, else, finally
# ===============================

print("Exception Handling Practice")
print("----------------------------")


# -------------------------------
# Example 1 - Divide Two Numbers
# -------------------------------

print("\nExample 1")

try:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ZeroDivisionError:

    print("You cannot divide by zero.")

except ValueError:

    print("Please enter numbers only.")

else:

    print("Answer =", result)

finally:

    print("Example 1 Finished")


# -------------------------------
# Example 2 - User Age
# -------------------------------

print("\nExample 2")

try:

    age = int(input("Enter your age: "))

except ValueError:

    print("Invalid age.")

else:

    print("Your age is", age)

finally:

    print("Example 2 Finished")


# -------------------------------
# Example 3 - File Open
# -------------------------------

print("\nExample 3")

try:

    file = open("student.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:

    print("File not found.")

finally:

    print("Example 3 Finished")


# -------------------------------
# Example 4 - Login
# -------------------------------

print("\nExample 4")

try:

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "abbas" and password == "1234":

        print("Login Successful")

    else:

        print("Invalid username or password")

except Exception:

    print("Something went wrong.")

finally:

    print("Login Process Finished")


# -------------------------------
# Example 5 - Student Marks
# -------------------------------

print("\nExample 5")

try:

    marks = int(input("Enter your marks: "))

except ValueError:

    print("Please enter valid marks.")

else:

    if marks >= 50:

        print("Pass")

    else:

        print("Fail")

finally:

    print("Example 5 Finished")


print("\nModule 2 Practice Completed.")