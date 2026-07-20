# ======================================
# Day 12 - Module 3
# Python List Methods
# ======================================

print("===== PYTHON LIST METHODS =====")

students = ["Abbas", "Ali", "Ahmed"]

print("\nOriginal List:")
print(students)

# append()
students.append("Usman")
print("\nAfter append():")
print(students)

# insert()
students.insert(1, "Ahsan")
print("\nAfter insert():")
print(students)

# remove()
students.remove("Ali")
print("\nAfter remove():")
print(students)

# pop()
students.pop()
print("\nAfter pop():")
print(students)

# sort()
students.sort()
print("\nAfter sort():")
print(students)

# reverse()
students.reverse()
print("\nAfter reverse():")
print(students)

# clear()
copy_students = students.copy()
copy_students.clear()

print("\nAfter clear():")
print(copy_students)