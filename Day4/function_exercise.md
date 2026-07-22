# Day 4 Exercises and Answers

This file turns the function practice questions from `function_exercise.py` into a simple learning guide.
Each section shows the question, a short explanation, and a clear example answer.

---

## 1. Add two numbers

**Question:** Declare a function named `add_two_numbers` that takes two parameters and returns their sum.

**Answer:**
```python
def add_two_numbers(a, b):
    return a + b

print(add_two_numbers(4, 5))
```

---

## 2. Area of a circle

**Question:** Write a function that calculates the area of a circle.

**Formula:** `area = pi × r × r`

**Answer:**
```python
import math

def area_of_circle(r):
    return math.pi * r * r

print(area_of_circle(3))
```

---

## 3. Sum all numbers

**Question:** Write a function called `add_all_nums` which takes an arbitrary number of arguments and sums all the arguments.

**Answer:**
```python
def add_all_nums(*args):
    total = 0
    for number in args:
        total += number
    return total

print(add_all_nums(1, 3, 4, 5))
```

---

## 4. Celsius to Fahrenheit

**Question:** Convert degrees Celsius to degrees Fahrenheit.

**Formula:** `°F = (°C × 9/5) + 32`

**Answer:**
```python
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

print(convert_celsius_to_fahrenheit(3))
```

---

## 5. Check season

**Question:** Write a function called `check_season` that takes a month parameter and returns the season.

**Answer:**
```python
def check_season(month):
    month = month.capitalize()

    if month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    elif month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    return 'Invalid month'

print(check_season('June'))
```

---

## 6. Calculate slope

**Question:** Write a function called `calculate_slope` which returns the slope of a linear equation.

**Formula:** `m = (y2 - y1) / (x2 - x1)`

**Answer:**
```python
def calculate_slope(y1, y2, x1, x2):
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(3, 2, 3, 1))
```

---

## 7. Quadratic equation value

**Question:** Write a function which calculates the value of a quadratic equation.

**Formula:** `ax² + bx + c`

**Answer:**
```python
def solve_quadratic_eqn(x, a, b, c):
    return a * x**2 + b * x + c

print(solve_quadratic_eqn(3, 10, 5, 2))
```

---

## 8. Print list items

**Question:** Declare a function named `print_list` that takes a list as a parameter and prints out each element.

**Answer:**
```python
def print_list(items):
    for item in items:
        print(item)

print_list([1, 2, 3, 4])
```

---

## 9. Reverse a list

**Question:** Declare a function named `reverse_list` that returns the reverse of an array.

**Answer:**
```python
def reverse_list(items):
    reversed_items = []
    for index in range(len(items) - 1, -1, -1):
        reversed_items.append(items[index])
    return reversed_items

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(['A', 'B', 'C']))
```

---

## 10. Capitalize list items

**Question:** Declare a function named `capitalize_list_items` that returns a capitalized list of items.

**Answer:**
```python
def capitalize_list_items(items):
    return [item.capitalize() for item in items]

print(capitalize_list_items(['a', 'b', 'c']))
```

---

## 11. Add an item to a list

**Question:** Declare a function named `add_item` that takes a list and an item and returns a list with the item added at the end.

**Answer:**
```python
def add_item(items, item):
    items.append(item)
    return items

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]

print(add_item(food_stuff, 'Meat'))
print(add_item(numbers, 5))
```

---

## 12. Remove an item from a list

**Question:** Declare a function named `remove_item` that takes a list and an item and returns a list with the item removed.

**Answer:**
```python
def remove_item(items, item):
    items.remove(item)
    return items

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]

print(remove_item(numbers, 2))
print(remove_item(food_stuff, 'Potato'))
```

---

## 13. Sum of numbers in a range

**Question:** Declare a function named `sum_of_numbers` that adds all the numbers in that range.

**Answer:**
```python
def sum_of_numbers(num):
    total = 0
    for value in range(1, num + 1):
        total += value
    return total

print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))
```

---

## 14. Sum of odd numbers

**Question:** Declare a function named `sum_of_odds` that adds all the odd numbers in a range.

**Answer:**
```python
def sum_of_odds(num):
    total = 0
    for value in range(1, num + 1):
        if value % 2 != 0:
            total += value
    return total

print(sum_of_odds(5))
```

---

## 15. Sum of even numbers

**Question:** Declare a function named `sum_of_even` that adds all the even numbers in a range.

**Answer:**
```python
def sum_of_even(num):
    total = 0
    for value in range(1, num + 1):
        if value % 2 == 0:
            total += value
    return total

print(sum_of_even(5))
```

---

## 16. Count evens and odds

**Question:** Write a function named `evens_and_odds` that counts the number of evens and odds in a positive integer.

**Answer:**
```python
def evens_and_odds(num):
    total_odd = 0
    total_even = 0

    for value in range(num + 1):
        if value % 2 != 0:
            total_odd += 1
        else:
            total_even += 1

    print(f'The number of odds are {total_odd}.')
    print(f'The number of evens are {total_even}.')

evens_and_odds(100)
```

---

## 17. Factorial

**Question:** Call your function `factorial` and return the factorial of the number.

**Answer:**
```python
import math

def factorial(num):
    if num >= 0:
        return math.factorial(num)
    return 'Factorial is not defined for negative numbers'

print(factorial(6))
```

---

## 18. Check if empty

**Question:** Write a function called `is_empty` that checks if a parameter is empty or not.

**Answer:**
```python
def is_empty(value):
    return value in ['', [], {}, None]

print(is_empty(''))
```

---

## 19. Median of a list

**Question:** Write a function that calculates the median of a list.

**Answer:**
```python
def calculate_median(items):
    items = sorted(items)
    n = len(items)

    if n % 2 != 0:
        return items[n // 2]

    mid1 = items[n // 2 - 1]
    mid2 = items[n // 2]
    return (mid1 + mid2) / 2

print(calculate_median([1, 2, 3, 4]))
```

---

## 20. Mode of grouped data

**Question:** Write a function that calculates the mode of grouped data.

**Answer:**
```python
def calculate_mode(l, h, fm, f1, f2):
    numerator = fm - f1
    denominator = (2 * fm) - f1 - f2

    if denominator == 0:
        return 'Mode is undefined (division by zero)'

    return l + (numerator / denominator) * h

print(calculate_mode(12, 2, 4, 6, 7))
```

---

## 21. Range of a list

**Question:** Write a function that calculates the range of a list.

**Answer:**
```python
def calculate_range(items):
    return max(items) - min(items)

print(calculate_range([77, 89, 92, 64, 78, 95, 82]))
```

---

## 22. Greet by name

**Question:** Write a function called `greet` that takes a default argument `name`.

**Answer:**
```python
def greet(name='Guest'):
    if not name.strip():
        return 'Hello, Guest!'
    return f'Hello, {name}!'

print(greet())
print(greet(''))
print(greet('Fayaz'))
```

---

## 23. Show keyword arguments

**Question:** Create a function called `show_args` to take arbitrary named arguments and print their names and values.

**Answer:**
```python
def show_args(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

show_args(name='Alice', age=30, city='New York')
```

---

## 24. Check if a number is prime

**Question:** Write a function called `is_prime` which checks if a number is prime.

**Answer:**
```python
def is_prime(num):
    if num < 2:
        return False
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True

print(is_prime(1))
```

---

## 25. Check if all items are unique

**Question:** Write a function that checks if all items in a list are unique.

**Answer:**
```python
def is_unique(items):
    return len(items) == len(set(items))

print(is_unique([1, 2, 3, 4, 5, 5]))
```

---

## 26. Check same data type

**Question:** Write a function that checks if all items in the list are of the same data type.

**Answer:**
```python
def same_datatype(items):
    if not items:
        return True
    return all(type(item) == type(items[0]) for item in items)

print(same_datatype([1, 2, 3, 4]))
```