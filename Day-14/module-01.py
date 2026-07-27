# ===============================
# Day 14 (Repeat)
# Module 1 - Exception Basics
# ===============================

print("===== Exception Handling Basics =====")


# -------------------------------
# Example 1 - ZeroDivisionError
# -------------------------------

print("\nExample 1")

try:

    number1 = 20
    number2 = 0

    answer = number1 / number2

    print(answer)

except ZeroDivisionError:

    print("You cannot divide a number by zero.")


# -------------------------------
# Example 2 - ValueError
# -------------------------------

print("\nExample 2")

try:

    age = int(input("Enter your age: "))

    print("Your age is", age)

except ValueError:

    print("Please enter numbers only.")


# -------------------------------
# Example 3 - NameError
# -------------------------------

print("\nExample 3")

try:

    print(city)

except NameError:

    print("Variable 'city' is not defined.")


# -------------------------------
# Example 4 - TypeError
# -------------------------------

print("\nExample 4")

try:

    result = 10 + "20"

    print(result)

except TypeError:

    print("You cannot add an integer and a string.")


# -------------------------------
# Example 5 - IndexError
# -------------------------------

print("\nExample 5")

try:

    numbers = [10, 20, 30]

    print(numbers[5])

except IndexError:

    print("Index is out of range.")


# -------------------------------
# Example 6 - KeyError
# -------------------------------

print("\nExample 6")

try:

    student = {
        "name": "Abbas",
        "age": 22
    }

    print(student["marks"])

except KeyError:

    print("This key does not exist in the dictionary.")


# -------------------------------
# Example 7 - FileNotFoundError
# -------------------------------

print("\nExample 7")

try:

    file = open("data.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:

    print("File not found.")


print("\nModule 1 Practice Completed.")