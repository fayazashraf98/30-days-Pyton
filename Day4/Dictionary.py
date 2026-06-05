"""Examples and exercises demonstrating Python dictionaries.

This file shows how to create, access, modify, iterate, and copy
dictionary objects, including nested dictionaries and common methods.
"""

from pprint import pprint

# Demonstrate an empty dictionary literal and its type
print({})
print(type({}))  # Empty dict

# Create an empty dict using the constructor
d = dict()
print(d)
print(type(d))

# A small dictionary mapping Finnish words to English
finish_to_english = {
    'talo': 'house',
    'kirja': 'book',
    'mies': 'man',
    'ninen': 'woman',
    'poika': 'boy',
}

# A nested dictionary representing a person with lists/tuples and an address
person = {
    'first_name': "Muhammad",
    'last_name': "Fayaz",
    'age': 26,
    'is_married': False,
    'country': "Romania",
    'kinds': ('john', 'Robert', 'Marta'),
    'schools': ['DC', 'Iqra', 'UPB'],
    'skills': ['python', 'IOS', 'Flutter'],
    'hobbies': ['Hikking', 'fishing', 'Football'],
    'address': {
        'city': 'Buchrest',
        'street_name': 'p22 street',
        'zipcode': "02270",
    }
}

# Pretty-print the person dict for readability
pprint(person)

# Accessing values and working with sequences inside the dict
print(person['age'])
print(person['skills'])
print(len(person['skills']))

# Add a new top-level key
person['nationality'] = 'Pakistan'

# Modify a nested list (append a new school)
person['schools'].append('Govt')

pprint(person)

# Safely retrieve a value with `get` (returns None if key missing)
print(person.get('schools'))

# Membership test before accessing a key
if 'hobbies' in person:
    print(person['hobbies'])

# Number of keys in the person dictionary
print(len(person))

# Dictionary view objects for keys, values and items
print(finish_to_english.keys())
print(finish_to_english.values())
print(finish_to_english.items())

# Iterate over (key, value) pairs
for item in finish_to_english.items():
    print(item, item[0], item[1])

    # Inside the loop demonstrate iterating over another dict
    for key in person:
        print(key, person[key])

# Remove entries using pop() and del
finish_to_english.pop('poika')
print(finish_to_english)
del finish_to_english['talo']
print(finish_to_english)

# Make a shallow copy of the person dictionary
person_data_copied = person.copy()
