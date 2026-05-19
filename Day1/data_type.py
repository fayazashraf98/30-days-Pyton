# ============================================================================
# Data Types - Day 1
# ============================================================================
# This file demonstrates common Python data types with examples and comments
# to help beginners understand how to use them.
# ============================================================================

print("=" * 60)
print("Python Data Types - Examples")
print("=" * 60)
print()

# ---------- Numbers ----------
# Integers, floats and complex numbers
print("-- Numbers --")
print("Integer:", 10, "->", type(10))
print("Float:", 10.1, "->", type(10.1))
print("Complex:", 10 + 10j, "->", type(10 + 10j))
print()

# ---------- Strings ----------
print("-- Strings --")
name = 'Muhammad Fayaz'
print("String value:", name)
print("Type:", type(name))
print("Example string:", "I am a student and I am learning Python")
print(f"Length of '{name}':", len(name))
print()

# ---------- Lists ----------
# Ordered, mutable collection
print("-- Lists --")
fruits = ['Milk', 'Coffee', 'Shake', 'Chai']
print("List:", fruits)
print("Type:", type(fruits))
print()

# ---------- Tuples ----------
# Ordered, immutable collection
print("-- Tuples --")
tpl = (1, 2, 3, 4, 5)
print("Tuple:", tpl)
print("Type:", type(tpl))
print()

# ---------- Sets ----------
# Unordered collection of unique values
print("-- Sets --")
st = {1, 2, 3, 4, 5}
print("Set:", st)
print("Type:", type(st))
print()

# ---------- Dictionaries ----------
# Key-value mappings
print("-- Dictionaries --")
user = {
    'userName': 'Tooba Khurram',
    'age': 27,
    'address': 'PIB, Karachi'
}
print("Dictionary:", user)
print("Type:", type(user))
print()

print("=" * 60)
print("End of data types examples")
print("=" * 60)
