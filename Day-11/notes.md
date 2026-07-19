# Day 11 Notes

## Topics Learned

- While Loop
- While Loop Syntax
- Difference Between for Loop and while Loop
- Infinite Loop
- break Statement
- continue Statement
- pass Statement

---

## What is a While Loop?

A while loop repeatedly executes a block of code as long as the given condition is True.

Syntax:

```python
while condition:
    # Code
```

---

## Difference Between for and while Loop

### for Loop

- Used when the number of iterations is known.
- Uses range() frequently.

Example:

```python
for i in range(5):
    print(i)
```

### while Loop

- Used when the number of iterations is unknown.
- Runs until the condition becomes False.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Infinite Loop

An infinite loop happens when the condition never becomes False.

Example:

```python
while True:
    print("Running...")
```

---

## break Statement

Stops the loop immediately.

Example:

```python
while True:
    break
```

---

## continue Statement

Skips the current iteration and moves to the next one.

Example:

```python
count = 0

while count < 5:
    count += 1

    if count == 3:
        continue

    print(count)
```

---

## pass Statement

Acts as a placeholder. It does nothing.

Example:

```python
if True:
    pass
```

---

## AI Applications

- AI Chatbots
- Voice Assistants
- Automation Systems
- AI Agents
- Menu Driven Programs
- Games
- Background Services

---

## Key Learning

- while loop is condition-based.
- break stops the loop.
- continue skips the current iteration.
- pass is a placeholder.
- while loops are widely used in AI systems and automation.