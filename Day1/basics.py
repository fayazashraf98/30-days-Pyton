# ============================================================================
# Python Basics - Day 1: 30 Days of Python Challenge
# ============================================================================
# This script demonstrates fundamental Python built-in functions
# and concepts that every beginner should understand.
# ============================================================================

print("=" * 70)
print("Welcome to Python Basics - Day 1 of 30 Days of Python Challenge!")
print("=" * 70)
print()

# --- INTRODUCTION: The print() Function ---
# print() is a built-in function that outputs text to the console
# It can accept multiple arguments separated by commas

print("Example 1: print() function with mixed data types")
print('Hello', 'Python', True, 'Fruits:', ['Mango', 'Banana'], 1.5, 'KG')
print()

# --- WORKING WITH THE len() FUNCTION ---
# len() returns the number of characters in a string or elements in a list

print("-" * 70)
print("Example 2: len() function - Count characters in a string")
print("-" * 70)
print(f"Length of 'Fayaz': {len('Fayaz')}")
print()

print("Example 3: len() function - Count elements in a list")
fruits = ['Tomato', 'Potato', 'Milk']
print(f"Fruits list: {fruits}")
print(f"Number of fruits: {len(fruits)}")
print()

# --- WORKING WITH VARIABLES ---
# Variables are containers that store data values
# Uncomment the lines below to accept user input:
# firstName = input('Enter your Name: ')
# age = input('Enter your age: ')
# address = input('Enter your address: ')
# print(f'Name: {firstName}\nAge: {age}\nAddress: {address}')

# --- THE round() FUNCTION ---
# round() rounds a decimal number to the nearest integer

print("-" * 70)
print("Example 4: round() function - Round decimal numbers")
print("-" * 70)
print(f"round(9.8) = {round(9.8)}")
print(f"round(2.1) = {round(2.1)}")
print(f"round(4.51) = {round(4.51)}")
print(f"round(7.3) = {round(7.3)}")
print()

# --- COMMON BUILT-IN FUNCTIONS ---
# Python provides many useful functions. Here are the most important ones:
# abs(), int(), str(), sum(), min(), max(), type(), bool(), range(), id(), dir()

print("-" * 70)
print("Example 5: abs() function - Get absolute value (remove negative sign)")
print("-" * 70)
print(f"abs(-5) = {abs(-5)}")
print(f"abs(-15.5) = {abs(-15.5)}")
print()

# --- TYPE CONVERSION FUNCTIONS ---

print("-" * 70)
print("Example 6: int() function - Convert to integer")
print("-" * 70)
result = int('2') + 2
print(f"int('2') + 2 = {result}")
print()

print("-" * 70)
print("Example 7: str() function - Convert to string")
print("-" * 70)
number = 5
text = "The number is: " + str(number)
print(text)
print()

# --- LIST OPERATIONS ---

print("-" * 70)
print("Example 8: sum() function - Add all numbers in a list")
print("-" * 70)
numbers = [1, 2, 3, 4, 5]
print(f"List: {numbers}")
print(f"sum({numbers}) = {sum(numbers)}")
print()

print("-" * 70)
print("Example 9: min() and max() functions - Find smallest and largest values")
print("-" * 70)
values = [1, 2, 3, 4, 5, 6, 0]
print(f"Values: {values}")
print(f"min({values}) = {min(values)}")
print(f"max({values}) = {max(values)}")
print()

# --- IDENTIFYING DATA TYPES ---

print("-" * 70)
print("Example 10: type() function - Identify data type of values")
print("-" * 70)
print(f"type('Fayaz') = {type('Fayaz')}")          # String
print(f"type(21) = {type(21)}")                    # Integer
print(f"type(9.1) = {type(9.1)}")                  # Float
print(f"type([1,2,3]) = {type([1, 2, 3])}")       # List
print(f"type((1+1j)) = {type((1+1j))}")           # Complex number
print(f"type({{'id': 12}}) = {type({'id': 12})}") # Dictionary
print(f"type({{1, 2, 3}}) = {type({1, 2, 3})}")   # Set
print()

# --- BOOLEAN VALUES ---

print("-" * 70)
print("Example 11: bool() function - Working with True and False")
print("-" * 70)
print(f"type(1 > 0) = {type(1 > 0)}")  # Comparison returns boolean
print(f"True = {True}")
print(f"False = {False}")
print()

# --- THE range() FUNCTION ---
# range() creates a sequence of numbers
# Format: range(start, stop, step)

print("-" * 70)
print("Example 12: range() function - Generate sequences of numbers")
print("-" * 70)
sequence = list(range(0, 10, 1))
print(f"range(0, 10, 1) = {sequence}")
print()

# --- OBJECT IDENTITY ---

print("-" * 70)
print("Example 13: id() function - Get unique identifier of an object")
print("-" * 70)
print(f"id(1) = {id(1)}")
print(f"id('Python') = {id('Python')}")
print()

# --- EXPLORING OBJECT ATTRIBUTES ---

print("-" * 70)
print("Example 14: dir() function - List available methods and attributes")
print("-" * 70)
print(f"Methods available for strings (dir('fayaz')):")
print(dir("fayaz"))
print()

print("=" * 70)
print("End of Python Basics Tutorial - Keep Learning!")
print("=" * 70)


