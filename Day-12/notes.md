# Day 12 Notes

## Topics Learned

- Introduction to Lists
- List Indexing
- Positive Indexing
- Negative Indexing
- Accessing List Items
- Modifying List Items
- List Length
- Membership Operator (in)
- Loop Through Lists
- List Methods

---

# What is a List?

A List is a collection of multiple items stored in a single variable.

Example:

```python
students = ["Abbas", "Ali", "Ahmed"]
```

---

# Why Use Lists?

Instead of creating multiple variables, we can store many values inside one variable.

Without List:

```python
student1 = "Abbas"
student2 = "Ali"
student3 = "Ahmed"
```

With List:

```python
students = ["Abbas", "Ali", "Ahmed"]
```

---

# Indexing

Lists start from index 0.

Example:

```python
students = ["Abbas", "Ali", "Ahmed", "Usman"]
```

| Index | Value |
|-------|-------|
| 0 | Abbas |
| 1 | Ali |
| 2 | Ahmed |
| 3 | Usman |

Negative Index:

| Index | Value |
|-------|-------|
| -1 | Usman |
| -2 | Ahmed |
| -3 | Ali |
| -4 | Abbas |

---

# Access List Items

```python
print(students[0])
print(students[-1])
```

---

# Update List Item

```python
students[1] = "Ahsan"
```

---

# List Length

```python
print(len(students))
```

Returns the total number of items.

---

# Membership Operator

```python
print("Ali" in students)
```

Output:

```
True
```

---

# Loop Through a List

```python
for student in students:
    print(student)
```

---

# List Methods

## append()

Adds an item at the end.

```python
students.append("Usman")
```

---

## insert()

Adds an item at a specific index.

```python
students.insert(1, "Ahsan")
```

---

## remove()

Removes an item by value.

```python
students.remove("Ali")
```

---

## pop()

Removes an item by index.

```python
students.pop()

students.pop(2)
```

---

## clear()

Removes all items.

```python
students.clear()
```

---

## sort()

Sorts the list in ascending order.

```python
numbers.sort()
```

---

## reverse()

Reverses the list.

```python
numbers.reverse()
```

---

# AI Applications

Lists are widely used in AI projects.

Examples:

- Chat History
- User Messages
- Agent Memory
- Email Queue
- Search Results
- Tasks
- Documents
- Dataset Records

---

# Key Concepts

✔ List stores multiple values.

✔ Index starts from 0.

✔ Negative index starts from -1.

✔ append() adds items.

✔ insert() adds at a specific position.

✔ remove() deletes by value.

✔ pop() deletes by index.

✔ clear() removes everything.

✔ sort() sorts data.

✔ reverse() reverses data.

✔ Lists are one of the most important data structures in Python and AI.

---

# Interview Notes

Question:
What is a List?

Answer:
A List is a mutable data structure used to store multiple items inside a single variable.

---

Question:
Difference between append() and insert()?

Answer:

append() adds an item at the end.

insert() adds an item at a specific position.

---

Question:
Difference between remove() and pop()?

Answer:

remove() deletes by value.

pop() deletes by index.

---

Question:
Why are Lists important in AI?

Answer:

Lists help AI systems store and process collections of data such as messages, tasks, documents, datasets, search results, and conversation history.