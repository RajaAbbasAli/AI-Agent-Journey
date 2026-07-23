# Day 14 Mini Project
# Student Result Checker

print("===== Student Result Checker =====")

try:

    name = input("Enter Student Name: ")

    english = int(input("Enter English Marks: "))
    math = int(input("Enter Math Marks: "))
    science = int(input("Enter Science Marks: "))

    if english < 0 or english > 100:
        raise ValueError("English marks should be between 0 and 100.")

    if math < 0 or math > 100:
        raise ValueError("Math marks should be between 0 and 100.")

    if science < 0 or science > 100:
        raise ValueError("Science marks should be between 0 and 100.")

    total = english + math + science

    percentage = total / 3

    print("\n----- Result -----")
    print("Name :", name)
    print("Total Marks :", total)
    print("Percentage :", percentage)

    if percentage >= 80:
        print("Grade : A")

    elif percentage >= 70:
        print("Grade : B")

    elif percentage >= 60:
        print("Grade : C")

    elif percentage >= 50:
        print("Grade : D")

    else:
        print("Grade : Fail")

except ValueError as error:

    print(error)

finally:

    print("\nProgram Finished.")