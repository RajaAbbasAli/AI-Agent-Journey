# Day 13 - Module 2
# Reading and Writing Files

print("=== File Handling Practice ===")

# Step 1: File me data likhna

file = open("student.txt", "w")

file.write("Name : Abbas Ali\n")
file.write("Age : 20\n")
file.write("Course : Python\n")

file.close()

print("Data saved successfully.")

print("----------------------")

# Step 2: File read karna

file = open("student.txt", "r")

data = file.read()

print(data)

file.close()

print("----------------------")

# Step 3: Naya data add karna

file = open("student.txt", "a")

file.write("City : Lahore\n")
file.write("Goal : AI Engineer\n")

file.close()

print("New data added.")

print("----------------------")

# Step 4: Dobara file read karna

file = open("student.txt", "r")

print(file.read())

file.close()

print("----------------------")

# Step 5: with open() use karna

with open("student.txt", "r") as file:

    print("Reading file using with open()")
    print(file.read())

print("----------------------")

print("Program Finished.")