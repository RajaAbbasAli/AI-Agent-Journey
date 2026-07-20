# ======================================
# Day 12 - Module 2
# Accessing & Modifying Lists
# ======================================

print("===== LIST OPERATIONS =====")

students = ["Abbas", "Ali", "Ahmed", "Usman"]

print("\nOriginal List:")
print(students)

print("\nFirst Student:")
print(students[0])

print("\nLast Student:")
print(students[-1])

# Update Item
students[1] = "Ahsan"

print("\nUpdated List:")
print(students)

print("\nTotal Students:")
print(len(students))

print("\nChecking Student:")

if "Ahmed" in students:
    print("Ahmed Found")
else:
    print("Ahmed Not Found")

print("\nPrinting All Students:")

for student in students:
    print(student)

print("\nAdding New Student:")

new_student = input("Enter Student Name: ")

students.append(new_student)

print("\nFinal List:")
print(students)