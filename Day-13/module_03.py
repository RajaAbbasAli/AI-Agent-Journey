# Day 13 - Module 3
# Exception Handling, CSV and JSON

import csv
import json

print("===== Module 3 Practice =====")

# -----------------------------
# Program 1 : Try and Except
# -----------------------------

print("\nProgram 1")

try:
    file = open("student.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found.")

finally:
    print("Program 1 Finished")


# -----------------------------
# Program 2 : Create CSV File
# -----------------------------

print("\nProgram 2")

file = open("students.csv", "w", newline="")

writer = csv.writer(file)

writer.writerow(["Name", "Age", "City"])
writer.writerow(["Abbas", "20", "Lahore"])
writer.writerow(["Ali", "22", "Karachi"])
writer.writerow(["Sara", "19", "Islamabad"])

file.close()

print("CSV File Created")


# -----------------------------
# Program 3 : Read CSV File
# -----------------------------

print("\nProgram 3")

file = open("students.csv", "r")

reader = csv.reader(file)

for row in reader:
    print(row)

file.close()


# -----------------------------
# Program 4 : Create JSON File
# -----------------------------

print("\nProgram 4")

student = {
    "name": "Abbas Ali",
    "age": 20,
    "city": "Lahore",
    "course": "Python"
}

file = open("student.json", "w")

json.dump(student, file, indent=4)

file.close()

print("JSON File Created")


# -----------------------------
# Program 5 : Read JSON File
# -----------------------------

print("\nProgram 5")

file = open("student.json", "r")

data = json.load(file)

print(data)

file.close()

print("\nAll Programs Completed Successfully.")