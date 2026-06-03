

# Set in Python:
# A set is an unordered collection of unique values.
# It is useful when you want to remove duplicates or perform set operations.

# Create two sets
A = {1, 2, 3, 4, 5, 6, 9}
B = {3, 4, 5, 8, 9}

# Set operations:
# A & B -> intersection: values found in both sets
# A | B -> union: all unique values from both sets
# A - B -> difference: values in A but not in B
# B - A -> difference: values in B but not in A
# A ^ B -> symmetric difference: values in either set, but not both

# Loop through a set.
# A set does not preserve order, so the printed order may change.
for value in A:
    print(value)

# Add one item to a set.
A.add(44)
print(A)

# Add multiple items from an iterable.
A.update([7, 11, 15, 25])
print(A)

# Remove an item from a set.
B.remove(5)
print(B)

# Remove all items from a set.
B.clear()
print(B)


# Convert a list to a set to remove duplicates.
fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
print(set(fruits))


# Recreate the sets for more examples.
A = {1, 2, 3, 4, 5, 6, 9}
B = {3, 4, 5, 8, 9}

# Union: combine unique values from both sets.
print(A.union(B))
print(B.union(A))

# Intersection: common values in both sets.
print(A.intersection(B))
print(B.intersection(A))

# Difference: values that appear in one set but not the other.
print(A.difference(B))
print(B.difference(A))

# Symmetric difference: values that are in one set or the other, but not both.
print(A.symmetric_difference(B))
