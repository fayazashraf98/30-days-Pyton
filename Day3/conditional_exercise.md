# Day 3 Exercises and Answers

This file turns the Python conditional practice questions from `conditonal_exercise.py` into a simple learning guide.
Each section shows the question, a short explanation, and a clear example answer.

---

## 1. Driving age check

**Question:** Ask the user to enter their age. If the user is 18 or older, print that they are old enough to drive. If they are below 18, print how many years are left.

**Answer:**
```python
age = int(input("Enter your age: "))
current_age = 18 - age

if age >= 18:
    print("You are old enough to learn to drive.")
elif age < 0:
    print("Invalid age")
else:
    print(f"You need {current_age} more years to learn to drive.")
```

**Why:**
- `if` handles age 18 and above.
- `elif` catches invalid negative ages.
- `else` handles everyone below 18.

---

## 2. Compare ages

**Question:** Compare `my_age` and `your_age` and print who is older.

**Answer:**
```python
my_age = int(input("Enter my age: "))
your_age = int(input("Enter your age: "))
diff_age = abs(my_age - your_age)

if my_age > your_age:
    print(f"You are {diff_age} years older than me.")
elif my_age == your_age:
    print("We both have the same age.")
else:
    print(f"You are {diff_age} years elder than me.")
```

**Why:**
- `abs()` gives the difference as a positive number.
- The comparison uses `if`, `elif`, and `else` to handle all cases.

---

## 3. Compare two numbers

**Question:** Get two numbers from the user and print whether the first is greater, smaller, or equal to the second.

**Answer:**
```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a == b:
    print(f"{a} is equal to {b}")
else:
    print(f"{a} is smaller than {b}")
```

---

## 4. Grade system

**Question:** Write a program that gives a grade based on score.

**Answer:**
```python
score = float(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid input")
elif score <= 59:
    print("F")
elif score <= 69:
    print("D")
elif score <= 79:
    print("C")
elif score <= 89:
    print("B")
else:
    print("A")
```

**Why:**
- The score is checked from lowest range to highest range.
- Invalid values are handled first.

---

## 5. Season based on month

**Question:** Ask the user for a month and print the season.

**Answer:**
```python
month = input("Enter the month: ")

if month in ["September", "October", "November"]:
    print("Autumn")
elif month in ["December", "January", "February"]:
    print("Winter")
elif month in ["March", "April", "May"]:
    print("Spring")
elif month in ["June", "July", "August"]:
    print("Summer")
else:
    print("Invalid input")
```

---

## 6. Add fruit if missing

**Question:** Check whether a fruit exists in the list. If not, add it.

**Answer:**
```python
find_fruit = input("Enter the fruit: ")
fruits = ['banana', 'orange', 'mango', 'lemon']

if find_fruit in fruits:
    print(f"{find_fruit} already exists in the list")
else:
    fruits.append(find_fruit)
    print(f"New item added to the list: {fruits}")
```

**Why:**
- `in` checks membership.
- `append()` adds the new fruit to the end of the list.

---

## 7. Work with the person dictionary

**Question:** Use the `person` dictionary to check the middle skill, test for Python, identify the developer type, and print marriage/country information.

**Answer:**
```python
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    middle = len(skills) // 2
    print(skills[middle])

if 'skills' in person:
    skills = person['skills']
    if 'Python' in skills:
        print("Python is in the list")
    else:
        print("Not in the list")

if 'skills' in person:
    skills = person['skills']

    if 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
    elif 'JavaScript' in skills and 'React' in skills:
        print('He is a front end developer')
    else:
        print('unknown title')

if person['is_married'] == True and person['country'] == 'Finland':
    print(f"{person['first_name']} lives in {person['country']}. He is married")
```

**Why:**
- The code checks whether the dictionary has the `skills` key before using it.
- Multiple conditions are used to classify the person.
- The final check combines two conditions with `and`.

---

## Learning Tips

- Use `if`, `elif`, and `else` to cover all cases.
- Keep conditions simple and readable.
- Use `in` for membership checks in lists and strings.
- Use dictionaries when data has named fields.

---

## Summary

This exercise set covers:

- Age checks and comparisons
- Number comparisons
- Grading systems
- Seasons based on month input
- List membership updates
- Dictionary condition checks

It is a strong practice set for learning Python conditionals step by step.
