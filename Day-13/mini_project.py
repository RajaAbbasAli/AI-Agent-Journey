# Day 13 Mini Project
# Personal Notes Manager

print("===== Personal Notes Manager =====")

while True:

    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        note = input("Write your note: ")

        file = open("notes.txt", "a")

        file.write(note + "\n")

        file.close()

        print("Note Saved Successfully!")

    elif choice == "2":

        try:

            file = open("notes.txt", "r")

            print("\n----- Your Notes -----")
            print(file.read())

            file.close()

        except FileNotFoundError:

            print("No notes found.")

    elif choice == "3":

        print("Thank You!")
        break

    else:

        print("Invalid Choice. Try Again.")