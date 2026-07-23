# Day 14 Notes

# Exception Handling in Python

## What is Exception Handling?

Exception Handling is used to stop a program from crashing when an error occurs.

Instead of closing the program, Python shows a message and continues the program.

---

# What is an Error?

An error is a problem in a program.

Some errors happen before running the program and some happen while the program is running.

---

# Types of Errors

## 1. Syntax Error

This happens when Python syntax is incorrect.

Example

```python
print("Hello"
```

---

## 2. Runtime Error

This happens while the program is running.

Example

```python
num = 10 / 0
```

Output

```
ZeroDivisionError
```

---

# Common Exceptions

- NameError
- TypeError
- ValueError
- ZeroDivisionError
- IndexError
- KeyError
- FileNotFoundError

---

# try Block

The code that may produce an error is written inside the try block.

Example

```python
try:

    num = 10 / 0
```

---

# except Block

If an error occurs, except block will run.

Example

```python
try:

    num = 10 / 0

except:

    print("Something went wrong.")
```

---

# Specific Exception

It is better to catch a specific error.

```python
try:

    age = int(input("Enter Age: "))

except ValueError:

    print("Invalid Input")
```

---

# Multiple except

More than one error can be handled.

```python
try:

    number = int(input("Enter Number"))

    print(10 / number)

except ValueError:

    print("Invalid Number")

except ZeroDivisionError:

    print("Cannot divide by zero")
```

---

# else Block

Else runs only when there is no error.

```python
try:

    age = int(input("Enter Age"))

except ValueError:

    print("Invalid Input")

else:

    print(age)
```

---

# finally Block

Finally always runs.

```python
try:

    print("Program Started")

finally:

    print("Program Finished")
```

---

# raise Keyword

Raise is used to create our own error.

Example

```python
age = -5

if age < 0:

    raise ValueError("Invalid Age")
```

---

# assert Statement

Assert checks a condition.

Example

```python
age = 20

assert age >= 18
```

---

# Input Validation

Validation means checking user input before using it.

Examples

- Age should not be negative.
- Marks should be between 0 and 100.
- Password should have at least 8 characters.
- Email should contain @.

---

# Real Life Examples

- ATM Machine
- Banking System
- Student Result System
- Login Page
- Online Forms
- AI Applications

---

# What I Learned

- Difference between Error and Exception.
- Compile Time Error.
- Runtime Error.
- try block.
- except block.
- else block.
- finally block.
- raise keyword.
- assert statement.
- Input Validation.
- Common Python Exceptions.

---

# Important Points

- try contains risky code.
- except handles errors.
- else runs if no error occurs.
- finally always executes.
- raise creates custom exceptions.
- Validation makes programs safer.

---

# Interview Questions

### What is Exception Handling?

Exception Handling is a way to handle runtime errors without stopping the program.

---

### Why do we use try and except?

To prevent the program from crashing when an error occurs.

---

### What is the purpose of else?

Else runs only when no exception occurs.

---

### What is finally?

Finally always runs whether an exception occurs or not.

---

### What is raise?

Raise is used to manually create an exception.

---

### Why is validation important?

Validation checks user input and prevents invalid data from entering the program.

---

# My Notes

Today I learned how to handle errors in Python. I practiced using try, except, else, finally and raise. I also understood that validating user input is very important because it helps make programs more reliable and user-friendly.