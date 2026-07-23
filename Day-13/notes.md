# Day 13 Notes

# File Handling in Python

## What is File Handling?

File Handling means working with files using Python.

With File Handling we can:

- Create a file
- Read a file
- Write data
- Add new data
- Save information permanently

---

## Why File Handling?

Normally, when a Python program closes, all variables are removed from memory.

Example:

```python
name = "Abbas"
```

After closing the program, this value is lost.

If we save it in a file, it stays even after the program ends.

---

## Types of Files

### Text Files

These files can be opened and read easily.

Examples:

- notes.txt
- student.txt
- README.md
- data.csv
- info.json

---

### Binary Files

These files cannot be read directly by humans.

Examples:

- image.jpg
- video.mp4
- song.mp3
- file.pdf

---

# open() Function

Python uses the `open()` function to work with files.

Syntax:

```python
open("filename", "mode")
```

Example:

```python
file = open("notes.txt", "r")
```

---

# File Modes

## Read Mode (r)

Used to read a file.

```python
file = open("notes.txt", "r")
print(file.read())
file.close()
```

---

## Write Mode (w)

Creates a new file.

If the file already exists, old data is removed.

```python
file = open("notes.txt", "w")

file.write("Hello Python")

file.close()
```

---

## Append Mode (a)

Adds new data at the end of a file.

Old data is not deleted.

```python
file = open("notes.txt", "a")

file.write("\nLearning File Handling")

file.close()
```

---

## Create Mode (x)

Creates a new file.

If the file already exists, Python gives an error.

```python
file = open("student.txt", "x")
```

---

# Reading Methods

## read()

Reads the complete file.

```python
print(file.read())
```

---

## readline()

Reads only one line.

```python
print(file.readline())
```

---

## readlines()

Returns all lines as a list.

```python
print(file.readlines())
```

---

# Closing a File

Always close a file after using it.

```python
file.close()
```

This helps save memory and keeps the file safe.

---

# with open()

This is the better way to open files.

```python
with open("notes.txt", "r") as file:

    print(file.read())
```

The file closes automatically.

---

# Exception Handling

Sometimes a file does not exist.

Instead of crashing the program, we can use `try` and `except`.

Example:

```python
try:

    file = open("abc.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:

    print("File not found")
```

---

# finally

The `finally` block always runs.

```python
try:

    print("Opening File")

finally:

    print("Program End")
```

---

# CSV File

CSV stands for Comma Separated Values.

Example:

```
Name,Age,City
Abbas,20,Lahore
Ali,22,Karachi
```

CSV is commonly used for tables and Excel data.

---

# JSON File

JSON is used to store structured data.

Example:

```json
{
    "name": "Abbas",
    "age": 20,
    "city": "Lahore"
}
```

Many APIs use JSON.

---

# Real-Life Uses

- Student Record System
- Banking Software
- AI Agents
- Chat History
- Notes App
- Attendance System
- Automation Scripts

---

# What I Learned Today

- How to create a file
- How to read a file
- How to write data
- How to append new data
- Difference between r, w, a and x modes
- How to use with open()
- Basic Exception Handling
- Introduction to CSV
- Introduction to JSON

---

# Key Points

- `open()` opens a file.
- `read()` reads the file.
- `write()` writes data.
- `a` adds new data.
- `w` replaces old data.
- `with open()` is the recommended method.
- `try` and `except` help prevent program crashes.
- CSV stores table data.
- JSON stores structured data.

---

# Interview Questions

### What is File Handling?

File Handling is used to create, read, write and manage files in Python.

### Why do we use with open()?

Because it automatically closes the file.

### Difference between w and a?

- `w` removes old data and writes new data.
- `a` keeps old data and adds new data at the end.

### What is CSV?

CSV is a file format used to store tabular data.

### What is JSON?

JSON is a lightweight format used to store and exchange structured data.

---

# My Notes

Today I learned how Python stores data inside files instead of variables only. I also learned different file modes and basic exception handling. I understood that CSV is useful for table data and JSON is commonly used in APIs and AI applications.