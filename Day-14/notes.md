# 📝 Day 14 (Repeat) - Notes.md

# Topic
Exception Handling in Python (Repeat)

---

# What is an Exception?

An exception is an error that happens while the program is running.

Without exception handling, the program stops immediately.

With exception handling, the program continues running and shows a friendly error message.

---

# Error vs Exception

Error:
- A problem in the program.
- It can stop the program.

Exception:
- A runtime error.
- It can be handled using try and except.

---

# Common Python Exceptions

1. SyntaxError
2. NameError
3. TypeError
4. ValueError
5. ZeroDivisionError
6. FileNotFoundError
7. IndexError
8. KeyError
9. AssertionError

---

# try

The try block contains code that might produce an error.

Example

try:
    number = 10 / 0

except:
    print("Error")

---

# except

The except block handles the error.

It prevents the program from crashing.

---

# else

The else block runs only if no error occurs.

Example

try:
    age = int(input())

except ValueError:
    print("Invalid Input")

else:
    print("Age Accepted")

---

# finally

The finally block always runs.

It is commonly used for cleanup work.

Example

try:
    print("Program Started")

finally:
    print("Program Finished")

---

# raise

The raise keyword is used to create an exception manually.

Example

if age < 0:
    raise ValueError("Age cannot be negative.")

---

# assert

Assert checks whether a condition is True.

If the condition is False, Python raises an AssertionError.

Example

assert marks >= 0

---

# Input Validation

Validation means checking user input before using it.

Examples

✔ Age should not be negative.

✔ Marks should be between 0 and 100.

✔ Password should contain at least 8 characters.

✔ Email should contain @.

---

# Why Validation is Important?

- Prevents invalid data.
- Makes programs safer.
- Improves user experience.
- Reduces runtime errors.

---

# Best Practices

- Use specific exceptions.
- Keep the try block small.
- Display clear error messages.
- Validate user input.
- Use finally when needed.
- Don't trust user input.

---

# Real-Life Uses

- ATM Machine
- Banking Software
- Hospital Management System
- School Result System
- Online Shopping Websites
- AI Applications

---

# What I Practiced Today

- try
- except
- else
- finally
- raise
- assert
- ValueError
- ZeroDivisionError
- FileNotFoundError
- NameError
- TypeError
- IndexError
- KeyError
- Input Validation

---

# Key Takeaways

✔ Exceptions happen during program execution.

✔ try is used for risky code.

✔ except handles errors.

✔ else runs only when no error occurs.

✔ finally always executes.

✔ raise creates a custom exception.

✔ assert checks conditions.

✔ Input validation is important in every real-world application.

---

# Interview Questions

Q1. What is Exception Handling?

Exception handling is a technique used to prevent a program from crashing when an error occurs.

Q2. What is the difference between Error and Exception?

Error is a general problem, while an Exception is a runtime error that can be handled.

Q3. Why do we use try and except?

To handle runtime errors without stopping the program.

Q4. What is raise?

It is used to manually create an exception.

Q5. Why is input validation important?

It ensures that only valid data is accepted by the program.

---

# My Learning Summary

Today I revised Python Exception Handling.

I learned how to use try, except, else, finally, raise, and assert. I also practiced input validation and understood how professional programs prevent crashes by handling user errors properly.