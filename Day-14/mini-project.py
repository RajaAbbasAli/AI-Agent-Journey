# ==========================================
# Mini Project
# Student Result Management System
# ==========================================

print("===================================")
print(" Student Result Management System ")
print("===================================")

try:

    # Student Name
    name = input("Enter student name: ")

    # Subject Marks
    english = int(input("Enter English Marks: "))
    math = int(input("Enter Math Marks: "))
    science = int(input("Enter Science Marks: "))

    # Validation
    if english < 0 or english > 100:
        raise ValueError("English marks must be between 0 and 100.")

    if math < 0 or math > 100:
        raise ValueError("Math marks must be between 0 and 100.")

    if science < 0 or science > 100:
        raise ValueError("Science marks must be between 0 and 100.")

    # Total
    total = english + math + science

    # Percentage
    percentage = total / 3

    # Grade
    if percentage >= 80:
        grade = "A"

    elif percentage >= 70:
        grade = "B"

    elif percentage >= 60:
        grade = "C"

    elif percentage >= 50:
        grade = "D"

    else:
        grade = "F"

    # Result
    print("\n========== RESULT ==========")

    print("Student Name :", name)
    print("English      :", english)
    print("Math         :", math)
    print("Science      :", science)
    print("----------------------------")
    print("Total Marks  :", total)
    print("Percentage   :", round(percentage, 2), "%")
    print("Grade        :", grade)

    if grade == "F":
        print("Status       : Fail")

    else:
        print("Status       : Pass")

except ValueError as error:

    print("\nError:", error)

finally:

    print("\nProgram Finished.")