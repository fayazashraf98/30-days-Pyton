
# ============================================================================
# Strings in Python
# ============================================================================
# A string is a text data type. Strings can be created with single quotes (' ')
# or double quotes (" ").
# ============================================================================

# --- Basic string examples ---
letters = 'abcdefghijklmnopqrstuvqxyz'
vowels = 'aeiou'

print("Letters:", letters)
print("Length of letters:", len(letters))
print("Vowels:", vowels)
print("Length of vowels:", len(vowels))
print("Uppercase letters:", letters.upper())
print("Uppercase vowels:", vowels.upper())
print("Available methods for a string:", dir(letters))
print()

# --- String formatting methods ---
# title() capitalizes the first letter of each word
# swapcase() changes uppercase letters to lowercase and vice versa

challenge = '30 Days of Python'
print("Original challenge string:", challenge)
print("Uppercase:", challenge.upper())
print("Title case:", challenge.title())
print("Swap case:", challenge.swapcase())
print("Find the character '0':", challenge.find('0'))
print()

# --- String indexing and slicing ---
language = 'Python'
print("Language:", language)
print("First two characters:", language[0:2])
print("Characters from index 2 onward:", language[2:])
print("Last three characters:", language[-3:])
print("Count of letter 'o':", language.count('o'))
print()

# --- String methods with spaces and character counting ---
city = ' mississippi '
print("City value with spaces:", repr(city))
print("Count of 'i':", city.count('i'))
print("Count of 'm':", city.count('m'))
print("Count of 's':", city.count('s'))
print("Count of 'p':", city.count('p'))
print("Trimmed city:", city.strip())
print("First index of 's':", city.find('s'))
print("List of characters:", list(city))
print("Index of 'i':", city.index('i'))
print()

# --- Start and end checks ---
country = 'finland'
print("Country:", country)
print("Starts with 'Fin':", country.startswith('Fin'))
print("Starts with 'f':", country.startswith('f'))
print("Ends with 'd':", country.endswith('d'))
print("Ends with 'land':", country.endswith('land'))
print()

# --- Joining and checking character types ---
skills = ['HTML', 'CSS', 'JS', 'Python']
print("Skills list:", skills)
print("Joined skills:", ', '.join(skills))
print()

print("Character checks:")
print("'abcd'.isalpha() ->", 'abcd'.isalpha())
print("'abc123'.isalpha() ->", 'abc123'.isalpha())
print("'123'.isnumeric() ->", '123'.isnumeric())
print("'123'.isdecimal() ->", '123'.isdecimal())
print("'123'.isdigit() ->", '123'.isdigit())
print()

# --- Replacing text in a sentence ---
sentence = "I love JavaScript. JavaScript is one of the most important things in the world."
print("Original sentence:")
print(sentence)
print("Updated sentence:")
print(sentence.replace('JavaScript', 'Python'))
print()

# --- Working with variables and f-strings ---
first_name = "Muhammad"
last_name = "Fayaz"
age = 25
country = "Romania"
city = "Bucharest"
skills = ['HTML', 'CSS', 'JS']

formatted_skills = ', '.join(skills)
full_name = first_name + ' ' + last_name

print("Full name:", full_name)
print(
	f"I am {full_name}, I am {age} years old, I live in {city}, {country}, "
	f"and I have {formatted_skills} job skills."
)
print()

# --- Splitting text into a list ---
sentence = 'I love Python'
print("Sentence:", sentence)
print("Split sentence:", sentence.split())
