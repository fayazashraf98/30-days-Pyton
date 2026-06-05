dog={}
"""Dictionary exercises with answers.

Each block implements an exercise and places the original question
as a comment directly under the answer (so the question appears
after its corresponding code). This makes the implementation easy
to read: you see the solution first, then the question for context.
"""

# 1) Create an empty dictionary called `dog`
dog = {}
print(dog)  # prints: {}
# Question 1: Create an empty dictionary called dog


# 2) Add name, color, breed, legs, age to the `dog` dictionary
dog = {
    'name': 'tiger',
    'color': 'brown',
    'breed': 'german',
    'legs': 4,
    'age': 10,
}
print(dog)
# Question 2: Add name, color, breed, legs, age to the dog dictionary


# 3) Create a `student` dictionary with requested keys (nested address)
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
# Question 3: Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary


# 4) Get the length of the student dictionary (number of top-level keys)
print(len(student))
# Question 4: Get the length of the student dictionary


# 5) Get the value of `skills` and check the data type (should be a list)
print(type(student.get("skills")))
# Question 5: Get the value of skills and check the data type, it should be a list


# 6) Modify the `skills` values by adding one or two skills
student['skills'].extend(["AI", "ML"])
print(student.get("skills"))
# Question 6: Modify the skills values by adding one or two skills


# 7) Get the dictionary keys as a list (dict_keys view is returned)
print(student.keys())
# Question 7: Get the dictionary keys as a list


# 8) Get the dictionary values as a list (dict_values view is returned)
print(student.values())
# Question 8: Get the dictionary values as a list


# 9) Change the dictionary to a list of tuples using `items()` method
print(list(student.items()))
# Question 9: Change the dictionary to a list of tuples using items() method


# 10) Delete one of the items in the dictionary (remove 'gender')
del student['gender']
print(student)
# Question 10: Delete one of the items in the dictionary


# 11) Delete one of the dictionaries (`dog`) to demonstrate deletion
del dog
try:
    print(dog)
except NameError:
    print('dog has been deleted')
# Question 11: Delete one of the dictionaries
