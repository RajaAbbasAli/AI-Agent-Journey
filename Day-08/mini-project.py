print("===== AI Interview Eligibility Checker =====")

age = int(input("Enter your age: "))
experience = int(input("Enter your years of experience: "))
english = input("Do you know English? (yes/no): ").lower()

if age >= 18 and experience >= 1 and english == "yes":
    print("✅ Congratulations!")
    print("You are eligible for the AI Engineer Interview.")
else:
    print("❌ Sorry!")
    print("You are not eligible for the interview.")