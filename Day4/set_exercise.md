# Set Exercises

This file turns the `set_exercise.py` practice into a Markdown lesson with short explanations and commented code examples.

---

## Sets in Python

A set is an unordered collection of unique values.

Use a set when you want to:
- remove duplicates,
- check membership quickly,
- and work with set operations like union and intersection.

### Example data

```python
# Set of IT companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Two numeric sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# A list of ages with duplicates
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

---

## Level 1

### 1) Find the length of the set `it_companies`

```python
# Print how many companies are in the set
print(len(it_companies))
```

### 2) Add `Twitter` to `it_companies`

```python
# Add one item to a set
it_companies.add('Twitter')
print(it_companies)
```

### 3) Insert multiple IT companies at once

```python
# Add several items from a list
it_companies.update(['Meta', 'Quanrio', 'GMS'])
print(it_companies)
```

### 4) Remove one company from `it_companies`

```python
# Remove one item from the set
it_companies.remove('Google')
print(it_companies)
```

### 5) Difference between `remove()` and `discard()`

- `remove()` raises an error if the item does not exist.
- `discard()` does not raise an error if the item does not exist.

---

## Level 2

### 1) Join `A` and `B`

```python
# Combine unique items from both sets
print(A.union(B))
```

### 2) Find `A` intersection `B`

```python
# Show the values common to both sets
print(A.intersection(B))
```

### 3) Is `A` a subset of `B`?

```python
# Check whether every item in A is also in B
print(A.issubset(B))
```

### 4) Are `A` and `B` disjoint sets?

```python
# Check whether the two sets have no items in common
print(A.isdisjoint(B))
```

### 5) Join `A` with `B` and `B` with `A`

```python
# Union works the same no matter the order
print(A.union(B))
print(B.union(A))
```

### 6) What is the symmetric difference between `A` and `B`?

```python
# Items that are in one set or the other, but not both
print(A.symmetric_difference(B))
```

### 7) Delete the sets completely

```python
# Clear all items from the set
A.clear()
print(A)
```

---

## Level 3

### 1) Convert the ages to a set and compare the lengths

```python
# Convert the list to a set to remove duplicates
age_set = set(age)
print(f'Set: {age_set}, Len Set: {len(age_set)}, Len List: {len(age)}')
print(f'Is the set bigger than the list? {len(age_set) > len(age)}')
```

Because sets remove duplicates, the set length is usually smaller than or equal to the list length.

### 2) Explain the difference between string, list, tuple, and set

- String: text data, like `"hello"`
- List: ordered and changeable collection
- Tuple: ordered but not changeable
- Set: unordered collection of unique items

### 3) Count the unique words in a sentence

```python
# Split the sentence into words
sentence = 'I am a teacher and I love to inspire and teach people'
words = sentence.split()

# Convert to a set to remove duplicate words
unique_words = set(words)

# Print the number of unique words
print(len(unique_words))
```

The sentence has 10 unique words.

---

## Notes

- Use `set()` when you need uniqueness.
- Use `union()` to combine sets.
- Use `intersection()` to find common values.
- Use `difference()` to see what is missing from one set compared to another.
- Use `symmetric_difference()` to find values that are not shared.
