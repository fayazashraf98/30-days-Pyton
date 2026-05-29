# Loop Exercises — Explanations and Solutions

This file contains the loop exercises from `loops_exercide.py` with added comments and short explanations for each block.

---

## 1) Iterate 0 to 10 using `for` and `while` loops

For loop: simple and concise — `range(11)` yields 0..10.

```python
# For Loop: iterate 0..10
for i in range(11):
    print(i)
```

While loop: manually manage the loop counter and increment it.

```python
# While Loop: iterate 0..10
i = 0
while i < 11:
    print(i)
    i = i + 1
```

---

## 2) Iterate 10 to 0 using `for` and `while` loops

For loop: use a negative step to count down.

```python
# For Loop: countdown 10..0
for i in range(10, -1, -1):
    print(i)
```

While loop: initialize at 10 and decrement until 0.

```python
# While Loop: countdown 10..0
i = 10
while i >= 0:
    print(i)
    i = i - 1
```

---

## 3) Print a triangle made of `#` (7 lines)

Use a single loop; multiply the string `'#'` by the current line number.

```python
# Print a triangle with 7 rows
for i in range(1, 8):
    print('#' * i)
```

Notes: start the loop at 1 so the first line is a single `#`.

---

## 4) Use nested loops to print an 8x8 grid of `#`

Outer loop controls rows, inner loop prints each column on the same row using `end=' '`.

```python
# Print an 8x8 grid of '#'
for _ in range(8):
    for _ in range(8):
        print('#', end=' ')
    print()  # new line after each row
```

---

## 5) Print multiplication squares 0..10

Each line shows `n x n = n*n`.

```python
# Print squares from 0 to 10
for i in range(11):
    print(f'{i} x {i} = {i * i}')
```

---

## 6) Iterate through a list and print items

```python
# Example list iteration
lst = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in lst:
    print(item)
```

---

## 7) Print only even numbers from 0 to 100

```python
# Print even numbers from 0..100
for i in range(101):
    if i % 2 == 0:
        print(i)
```

## 8) Print only odd numbers from 0 to 100

```python
# Print odd numbers from 0..100
for i in range(101):
    if i % 2 != 0:
        print(i)
```

---

## 9) Sum of numbers from 0 to 100

Accumulate into a variable while looping.

```python
# Sum numbers 0..100
sum_of_num = 0
for i in range(101):
    sum_of_num += i
print('The sum of all numbers is', sum_of_num)
```

---

## 10) Sum of evens and odds from 0 to 100

Keep two accumulators and update them conditionally.

```python
# Sum of even and odd numbers 0..100
sum_of_even_num = 0
sum_of_odd_num = 0
for i in range(101):
    if i % 2 == 0:
        sum_of_even_num += i
    else:
        sum_of_odd_num += i
print(f'The sum of all evens is {sum_of_even_num}. And the sum of all odds is {sum_of_odd_num}')
```

---

## 11) Extract countries containing the word `land`

This assumes you have a `countries` list available (for example from `countries_list.py`). The search is case-sensitive; convert strings to lowercase if needed.

```python
# Given `countries` imported from countries_list
for country in countries:
    if 'land' in country:
        print(country)
```

Tip: to make the check case-insensitive, use `if 'land' in country.lower():`.

---

## Notes & style
- Prefer descriptive variable names (`i`, `j` are acceptable for small loop counters).
- Use `range(start, stop, step)` to control iteration direction and step size.
- Use `continue` to skip a single iteration and `break` to exit a loop early when conditions require it.

---

If you want, I can also:
- run the code and show output,
- convert this markdown into a nicely formatted PDF or notebook,
- or add inline explanations for each line of code.
