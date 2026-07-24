# Day 14 - Module 1
# Exception Handling Basics

print("===== Exception Handling Practice =====")

# Program 1

print("\nProgram 1")

try:

    num1 = 10
    num2 = 0

    print(num1 / num2)

except:

    print("Cannot divide by zero.")

print("----------------------")

# Program 2

print("\nProgram 2")

try:

    age = int(input("Enter your age: "))

    print("Age is", age)

except:

    print("Please enter numbers only.")

print("----------------------")

# Program 3

print("\nProgram 3")

try:

    print(name)

except:

    print("Variable not found.")

print("----------------------")

# Program 4

try:

    numbers = [10, 20, 30]

    print(numbers[5])

except:

    print("Index does not exist.")

print("----------------------")

# Program 5

try:

    student = {
        "name": "Abbas",
        "city": "Lahore"
    }

    print(student["age"])

except:

    print("Key not found.")

print("----------------------")

# Program 6

try:

    file = open("abc.txt", "r")

    print(file.read())

    file.close()

except:

    print("File not found.")

print("----------------------")

print("Module 1 Completed Successfully.")