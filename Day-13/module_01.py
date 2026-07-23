# Day 13 - Module 1
# Introduction to File Handling

print("=== File Handling Practice ===")

# File create karna aur us me data likhna

file = open("notes.txt", "w")

file.write("My Name is Abbas Ali.\n")
file.write("I am learning Python.\n")
file.write("Today I started File Handling.\n")

file.close()

print("File created successfully.")

print("------------------------")

# Ab file ko read karte hain

file = open("notes.txt", "r")

data = file.read()

print(data)

file.close()

print("------------------------")

print("Program Finished.")