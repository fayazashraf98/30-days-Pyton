

"""
Simple list examples and operations with inline explanations.

This file demonstrates creating lists, indexing, slicing, modifying,
and common methods like append, insert, pop, remove, clear, count and sorting.
"""

# Define a shopping list and show its contents and length
shoping_list = ['Milk', 'Tea', 'Coffee', 'Banana', 'Mango', 'Tomato']
print(shoping_list)        # print the whole list
print(len(shoping_list))   # print number of items in the list

# Numeric and string lists
nums = [1, 2, 3, 4, 5, 6]
names = ["Bill", "Steve", 'trump', "Elon"]
print(nums)
print(names)

# Mixed data types: lists can hold different types together
mixed_data = [0, 1, True, "Finland", "Sweden", ['trump', 'Bill']]
print(mixed_data)

# Indexing: access elements by their index (0-based)
nums = [1, 2, 3, 4, 5]
print(nums[0])            # first element
print(nums[1])            # second element
print(nums[2])            # third element
last_index = len(nums) - 1
print(last_index)         # index of the last element

# Slicing examples: extract sublists
print(nums[1:3])         # items at index 1 and 2
print(nums[2:5])         # items from index 2 up to 4
print(nums[2:])          # items from index 2 to the end
print(nums[::-1])        # reversed list (step -1)
print(nums[:3])          # first three items
print(nums[-3:-1])       # slice using negative indices

# Modifying elements by index
nums[0] = 10             # change first element
print(nums)
nums[2] = 33             # change third element
print(nums)

# Removing items with pop(): if no arg, removes last; with index removes that element
nums.pop()
print(nums)
nums.pop(0)              # remove first element
print(nums)
nums.pop(1)              # remove element at index 1
print(nums)

# Inserting items at a given position with insert(index, value)
nums.insert(1, 88)
print(nums)
nums.insert(2, 400)
print(nums)

# Membership test: check if a value exists in a list
countires = ['Finland', "Pakistan", "Norway"]
print('Finland' in countires)   # True if 'Finland' is in the list

# Append adds to the end of the list; demonstrate building a shopping list
shoping_list = []
print(len(shoping_list))
shoping_list.append('Milk')
shoping_list.append('Meat')
shoping_list.append('Tea')
shoping_list.append('Orange')
shoping_list.append('Pizza')
print(shoping_list)
shoping_list.remove('Pizza')   # remove by value
print(shoping_list)

# Use del to remove by index or slice
del shoping_list[0]
print(shoping_list)
del shoping_list[0:2]
print(shoping_list)

# Clear empties the list
shoping_list.clear()
print(shoping_list)

# Combine negative, zero and positive ranges to create a list of integers
positve_nums = [1, 2, 3, 4, 5, 6]
zero = [0]
negative_nums = [-1, -2, -3, -4, -5, -6]
integers = negative_nums[::-1] + zero + positve_nums
print(integers)

# Counting occurrences and finding index
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))    # how many times 24 appears
print(ages.index(24))    # index of first occurrence of 24

# Sorting without modifying original: sorted() returns a new list
sorted_age = sorted(ages)
print(sorted_age)

