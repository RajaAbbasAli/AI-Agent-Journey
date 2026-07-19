# ==========================================
# Day 11 Mini Project
# Smart ATM Simulation
# Created By: Abbas Ali
# ==========================================

balance = 5000

while True:

    print("\n==============================")
    print("      SMART ATM SYSTEM")
    print("==============================")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("==============================")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"\n💰 Your Current Balance: Rs. {balance}")

    elif choice == "2":
        amount = float(input("Enter Deposit Amount: Rs. "))

        if amount > 0:
            balance += amount
            print("✅ Deposit Successful!")
            print(f"New Balance: Rs. {balance}")
        else:
            print("❌ Invalid Amount!")

    elif choice == "3":
        amount = float(input("Enter Withdraw Amount: Rs. "))

        if amount <= balance:
            balance -= amount
            print("✅ Withdrawal Successful!")
            print(f"Remaining Balance: Rs. {balance}")
        else:
            print("❌ Insufficient Balance!")

    elif choice == "4":
        print("\nThank you for using Smart ATM.")
        print("Good Bye!")
        break

    else:
        print("❌ Invalid Choice! Please Try Again.")