# # sets


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# Find the length of the set it_companies
# Add 'Twitter' to it_companies
# Insert multiple IT companies at once to the set it_companies
# Remove one of the companies from the set it_companies
# What is the difference between remove and discard

print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)
it_companies.update(["Meta","Quanrio","GMS"])
print(it_companies)
it_companies.remove("Google")
print(it_companies)

#Both delete an element from a set, but if the element is not available, remove() raises an error while discard() does not raise any error.


# Exercises: Level 2

# Join A and B
# Find A intersection B
# Is A subset of B
# Are A and B disjoint sets
# Join A with B and B with A
# What is the symmetric difference between A and B
# Delete the sets completely


print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
print(A.clear)



# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# Explain the difference between the following data types: string, list, tuple and set
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

print(f'Set :{set(age)} Len Set: {len(set(age))},Len List: {len(age)} Is List Bigger:{len(set(age))>len(age)} ')


# A string is a sequence of characters (text).
# A list is a collection of items.
# A tuple is like a list but unchangeable.
#A set is a collection of unique items.
# String → text
# List → changeable collection
# Tuple → fixed list
# Set → unique items only



sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print(len(unique_words))

