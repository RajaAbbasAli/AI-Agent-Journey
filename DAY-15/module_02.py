# Day 14 - Module 2
# try, except, else and finally

print("===== Module 2 Practice =====")

# -----------------------------
# Program 1
# -----------------------------

print("\nProgram 1")

try:

    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    answer = num1 / num2

    print("Answer =", answer)

except ZeroDivisionError:

    print("Cannot divide by zero.")

except ValueError:

    print("Please enter numbers only.")

print("----------------------")


# -----------------------------
# Program 2
# -----------------------------

print("\nProgram 2")

try:

    age = int(input("Enter Your Age: "))

except ValueError:

    print("Invalid Age")

else:

    print("Your Age is", age)

print("----------------------")


# -----------------------------
# Program 3
# -----------------------------

print("\nProgram 3")

try:

    marks = int(input("Enter Your Marks: "))

    print("Marks =", marks)

except ValueError:

    print("Marks should be numbers.")

finally:

    print("Program Finished")

print("----------------------")


# -----------------------------
# Program 4
# -----------------------------

print("\nProgram 4")

try:

    file = open("student.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:

    print("File not found.")

finally:

    print("File Program Ended")

print("----------------------")


# -----------------------------
# Program 5
# -----------------------------

print("\nProgram 5")

try:

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "abbas" and password == "python123":

        print("Login Successful")

    else:

        print("Wrong Username or Password")

except:

    print("Something went wrong.")

finally:

    print("Login Program Finished")

print("----------------------")

print("Module 2 Completed Successfully.")