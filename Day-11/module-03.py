# ======================================
# Day 11 - Module 3
# break, continue and pass
# ======================================

print("===== BREAK EXAMPLE =====")

count = 1

while count <= 10:

    print(count)

    if count == 5:
        print("Loop Stopped!")
        break

    count += 1

print()

print("===== CONTINUE EXAMPLE =====")

count = 0

while count < 5:

    count += 1

    if count == 3:
        continue

    print(count)

print()

print("===== PASS EXAMPLE =====")

name = "Abbas"

if name == "Ali":
    print("Hello Ali")
else:
    pass

print("Program Finished!")