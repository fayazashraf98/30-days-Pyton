# Day 3 Exercises and Answers

This file turns the list practice questions from `list_exercise.py` into a simple learning guide.
Each section shows the question, a short explanation, and a clear example answer.

---

## 1. Declare an empty list

**Question:** Declare an empty list.

**Answer:**
```python
empty_list = []
print(empty_list)
```

---

## 2. Create a shopping list

**Question:** Declare a list with more than 5 items.

**Answer:**
```python
shopping_list = ["Banana", "Apple", "Grapes", "Mango", "Melon", "Orange", "Guava"]
print(shopping_list)
```

---

## 3. Find list length

**Question:** Find the length of your list.

**Answer:**
```python
print(len(shopping_list))
```

---

## 4. First, middle, and last item

**Question:** Get the first, middle and last item of the list.

**Answer:**
```python
print(shopping_list[0])
print(shopping_list[len(shopping_list) // 2])
print(shopping_list[-1])
```

---

## 5. Mixed data types list

**Question:** Create a list with mixed data types.

**Answer:**
```python
mixed_data_types = ["Muhammad Fayaz", 26, 168, "Single", "P22"]
print(mixed_data_types)
```

---

## 6. IT companies list

**Question:** Declare an `it_companies` list and print it with its length.

**Answer:**
```python
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'C', 'Amazon']
print(it_companies)
print(len(it_companies))
```

---

## 7. First, middle, and last company

**Question:** Print first, middle and last company from `it_companies`.

**Answer:**
```python
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])
```

---

## 8. Modify and insert companies

**Question:** Modify one company and insert new values.

**Answer:**
```python
it_companies[0] = 'Quanrio'
it_companies.insert(1, 'IT')
it_companies.insert(len(it_companies) // 2, 'IT')
print(it_companies)
```

---

## 9. Uppercase and join

**Question:** Convert one company name to uppercase and join the list with `#; `.

**Answer:**
```python
it_companies[0] = it_companies[0].upper()
print('#; '.join(it_companies))
```

---

## 10. Check if company exists

**Question:** Check if `Microsoft` exists in `it_companies`.

**Answer:**
```python
print('Microsoft' in it_companies)
```

---

## 11. Sort and reverse

**Question:** Sort numbers and reverse `it_companies` in descending order.

**Answer:**
```python
unsort_list = [4, 5, 23, 6, 42, 0, 7]
print(sorted(unsort_list))

it_companies.sort(reverse=True)
print(it_companies)
```

---

## 12. Slicing operations

**Question:** Slice first 3, last 3, and middle company.

**Answer:**
```python
print(it_companies[0:3])
print(it_companies[-3:])
mid = len(it_companies) // 2
print(it_companies[mid])
```

---

## 13. Remove companies step by step

**Question:** Remove first, middle, last and then clear all companies.

**Answer:**
```python
it_companies.pop(0)
middle = len(it_companies) // 2
it_companies.pop(middle)
it_companies.pop(middle - 1)
it_companies.pop()
it_companies.clear()
print(it_companies)
```

---

## 14. Join front-end and back-end lists

**Question:** Join `front_end` and `back_end` lists.

**Answer:**
```python
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
print(front_end + back_end)
```

---

## 15. Build full stack list

**Question:** Create `full_stack` and insert `Python` and `SQL` after `Redux`.

**Answer:**
```python
full_stack = front_end + back_end
index = full_stack.index('Redux')
full_stack.insert(index + 1, 'Python')
full_stack.insert(index + 2, 'SQL')
print(full_stack)
```

---

## 16. Age statistics

**Question:** Sort ages and find min, max, median, and average.

**Answer:**
```python
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()

print('Min age:', min(ages))
print('Max age:', max(ages))

n = len(ages)
mid = n // 2
if n % 2 == 0:
    median = (ages[mid - 1] + ages[mid]) / 2
else:
    median = ages[mid]

average = sum(ages) / len(ages)
print('Median age:', median)
print('Average age:', average)
```

---

## 17. Middle country and split countries list

**Question:** Find middle country(ies) and split countries into two halves.

**Answer:**
```python
from countries_list import countries

mid = len(countries) // 2

# middle country or countries
if len(countries) % 2 == 0:
    print(countries[mid - 1:mid + 1])
else:
    print(countries[mid])

# split into two halves (first half gets extra if odd)
if len(countries) % 2 == 0:
    first_half = countries[:mid]
    second_half = countries[mid:]
else:
    first_half = countries[:mid + 1]
    second_half = countries[mid + 1:]

print(first_half)
print(second_half)
```

---

## Learning Tips

- Use `len()` to find size quickly.
- Use `index` and slicing carefully to avoid out-of-range errors.
- Use list methods (`append`, `insert`, `pop`, `remove`, `clear`) based on your need.
- Prefer readable variable names and simple print statements while learning.

---

## Summary

This exercise set covers:

- Creating and accessing lists
- Updating and removing list items
- Sorting and slicing
- Joining multiple lists
- Basic statistics from list values
- Working with an external list (`countries`)

It is a solid beginner-friendly practice set for Python lists.
