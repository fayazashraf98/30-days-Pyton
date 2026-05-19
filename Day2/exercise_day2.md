# Day 2 Exercises and Answers

This file turns the Python practice questions from `exercise_day2.py` into a simple learning guide.
Each section shows the question, a short explanation, and a clear example answer.

---

## 1. Triangle area

**Question:** Write a script that prompts the user to enter the base and height of a triangle and calculate the area.

**Formula:** `area = 0.5 × base × height`

**Answer:**
```python
base = float(input("Enter the base: "))
height = float(input("Enter the height: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)
```

---

## 2. Triangle perimeter

**Question:** Ask the user for side `a`, side `b`, and side `c` of a triangle and calculate the perimeter.

**Formula:** `perimeter = a + b + c`

**Answer:**
```python
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter is:", perimeter)
```

---

## 3. Rectangle area and perimeter

**Question:** Get the length and width of a rectangle. Calculate its area and perimeter.

**Formulas:**
- `area = length × width`
- `perimeter = 2 × (length + width)`

**Answer:**
```python
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
perimeter = 2 * (length + width)
print("Area =", area)
print("Perimeter =", perimeter)
```

---

## 4. Circle area and circumference

**Question:** Get the radius of a circle and calculate the area and circumference.

**Formulas:**
- `area = pi × r × r`
- `circumference = 2 × pi × r`

**Answer:**
```python
pi = 3.14
r = float(input("Enter the radius: "))
area = pi * r * r
circumference = 2 * pi * r
print("Area =", round(area, 2))
print("Circumference =", circumference)
```

---

## 5. Slope, x-intercept, and y-intercept of `y = 2x - 2`

**Question:** Calculate the slope, x-intercept, and y-intercept of the line.

**Answer:**
```python
slope = 2
y_intercept = -2
x_intercept = 1

print("Slope =", slope)
print("Y-Intercept =", y_intercept)
print("X-Intercept =", x_intercept)
```

**Why:**
- The equation is already in slope-intercept form: `y = mx + b`
- So `m = 2` and `b = -2`
- To find the x-intercept, set `y = 0`

---

## 6. Slope and Euclidean distance between two points

**Question:** Find the slope and Euclidean distance between point `(2, 2)` and point `(6, 10)`.

**Formula:**
- `slope = (y2 - y1) / (x2 - x1)`
- `distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)`

**Answer:**
```python
import math

x1 = 2
y1 = 2
x2 = 6
y2 = 10

slope = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("The slope is:", slope)
print("Euclidean distance is:", round(distance, 2))
```

---

## 7. Quadratic value

**Question:** Calculate the value of `y = x^2 + 6x + 9`. Try different values of `x` and find when `y = 0`.

**Answer:**
```python
value_x = int(input("Enter the x value: "))
value_y = value_x ** 2 + 6 * value_x + 9
print(value_y)
```

**Hint:**
This expression can be written as:
`y = (x + 3)²`
So `y` becomes `0` when `x = -3`.

---

## 8. Length of `python` and `dragon`

**Question:** Find the length of `'python'` and `'dragon'` and make a falsy comparison statement.

**Answer:**
```python
print('The length of "python":', len('python'))
print('The length of "dragon":', len('dragon'))
print('Is the length of python equal to dragon?:', len('python') == len('dragon'))
```

---

## 9. Check for `on` in both `python` and `dragon`

**Question:** Use the `and` operator to check if `'on'` is found in both `'python'` and `'dragon'`.

**Answer:**
```python
word1 = 'python'
word2 = 'dragon'
print('on' in word1 and 'on' in word2)
```

---

## 10. Check for `jargon` in a sentence

**Question:** Use the `in` operator to check if `jargon` is in the sentence.

**Answer:**
```python
sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)
```

---

## 11. Check that `on` is not in both words

**Question:** There is no `'on'` in both `dragon` and `python`.

**Answer:**
```python
py = 'python'
dr = 'dragon'
print('on' not in py and 'on' not in dr)
```

---

## 12. Convert the length of `python`

**Question:** Find the length of the text `python` and convert it to float and then to string.

**Answer:**
```python
text1 = "python"
print(len(text1))
print(float(len(text1)))
print(str(len(text1)))
```

---

## 13. Even or odd number

**Question:** How do you check if a number is even or not?

**Answer:**
```python
num1 = 2
if num1 % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Why:**
A number is even if the remainder after division by 2 is `0`.

---

## 14. Floor division check

**Question:** Check if the floor division of `7` by `3` is equal to the integer value of `2.7`.

**Answer:**
```python
floor_div = 7 // 3
con_val = int(2.7)
print(floor_div)
print(floor_div == con_val)
```

---

## 15. Compare types of `'10'` and `10`

**Question:** Check if the type of `'10'` is equal to the type of `10`.

**Answer:**
```python
type1 = '10'
type2 = 10
print(type(type1) == type(type2))
```

---

## 16. Check `int('9.8')` against `10`

**Question:** Check if `int('9.8')` is equal to `10`.

**Answer:**
```python
num1 = int(float('9.8'))
print(num1 == 10)
```

---

## 17. Employee pay

**Question:** Prompt the user to enter hours and rate per hour. Calculate the weekly pay.

**Formula:** `pay = hours × rate_per_hour`

**Answer:**
```python
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print("Your weekly earning is:", pay)
```

---

## 18. Seconds lived

**Question:** Write a script that prompts the user to enter years. Calculate the number of seconds a person can live. Assume a person can live 100 years.

**Answer:**
```python
ageYears = int(input("Number of years you have lived: "))
seconds = ageYears * (365 * 24 * 60 * 60)
print(seconds)
```

---

## Learning Tips

- Use `input()` for user interaction.
- Use `print()` to show results clearly.
- Keep variable names meaningful.
- Add comments so beginners can follow the logic.
- Use spaces around operators for readability.

---

## Summary

This exercise set covers:

- Geometry formulas
- Operators and comparisons
- Strings and membership checks
- Type conversion
- Conditionals
- Basic calculations

It is a good practice set for learning Python fundamentals step by step.
