# Dictionary Exercise — Questions & Answers

This document presents each exercise answer first (as runnable Python snippets), with the original question placed immediately below the answer.

---

## 1
```python
# Answer
 dog = {}
 print(dog)
```

_Question 1: Create an empty dictionary called dog_

---

## 2
```python
# Answer
 dog = {
     'name': 'tiger',
     'color': 'brown',
     'breed': 'german',
     'legs': 4,
     'age': 10,
 }
 print(dog)
```

_Question 2: Add name, color, breed, legs, age to the dog dictionary_

---

## 3
```python
# Answer
 student = {
     'first_name': "Muhammad",
     'last_name': "Fayaz",
     'gender': 'Male',
     'age': 26,
     'is_married': False,
     'skills': ['python', 'IOS', 'Flutter'],
     'country': "Romania",
     'city': "buchrest",
     'address': {
         'city': 'Buchrest',
         'street_name': 'p22 street',
         'zipcode': "02270",
     }
 }
 print(student)
```

_Question 3: Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary_

---

## 4
```python
# Answer
 print(len(student))
```

_Question 4: Get the length of the student dictionary_

---

## 5
```python
# Answer
 print(type(student.get("skills")))
```

_Question 5: Get the value of skills and check the data type, it should be a list_

---

## 6
```python
# Answer
 student['skills'].extend(["AI", "ML"])
 print(student.get("skills"))
```

_Question 6: Modify the skills values by adding one or two skills_

---

## 7
```python
# Answer
 print(student.keys())
```

_Question 7: Get the dictionary keys as a list_

---

## 8
```python
# Answer
 print(student.values())
```

_Question 8: Get the dictionary values as a list_

---

## 9
```python
# Answer
 print(list(student.items()))
```

_Question 9: Change the dictionary to a list of tuples using items() method_

---

## 10
```python
# Answer
 del student['gender']
 print(student)
```

_Question 10: Delete one of the items in the dictionary_

---

## 11
```python
# Answer
 del dog
 try:
     print(dog)
 except NameError:
     print('dog has been deleted')
```

_Question 11: Delete one of the dictionaries_
