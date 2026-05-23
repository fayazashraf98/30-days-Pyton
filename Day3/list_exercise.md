# List Exercises

## Description
This file contains exercises that demonstrate common Python list operations. The original `list_exercise.py` performs: declaration of lists, indexing and slicing, mixed data types, list modification (insert, update, delete), joining lists, sorting and reversing, finding min/max/median/average, and splitting lists. It also uses `countries` from `countries_list.py` for some exercises.

## Exercises / Questions
1. Declare an empty list named `empty_list`.
2. Create a `shopping_list` with at least 6 items and print it.
3. Find and print the length of `shopping_list`.
4. Print the first, middle and last items of `shopping_list`.
5. Create a `mixed_data_types` list containing your name, age, height (cm), marital status and a city/zip code. Print the list.
6. Create an `it_companies` list with the companies: Facebook, Google, Microsoft, Apple, IBM, C, Amazon. Print the list and its length.
7. Print the first, middle and last company from `it_companies`.
8. Change the first company name to `Quanrio` and print the updated list.
9. Insert a new company `'IT'` at index 1 and then insert another `'IT'` in the middle of the list. Print the list after each change.
10. Convert one company name (except `IBM`) to uppercase and print the result.
11. Join the `it_companies` list into a single string separated by `#; ` and print it.
12. Check whether `"Microsoft"` exists in `it_companies` and print the boolean result.
13. Given `unsort_list = [4,5,23,6,42,0,7]`, create a sorted version and print it.
14. Sort `it_companies` in descending order and print the result.
15. Slice out the first three companies, the last three companies, and the middle company (or companies) from `it_companies`.
16. Remove the first company, the middle company/companyies, and the last company from `it_companies`. Print the list after each removal.
17. Clear all companies from `it_companies` using a method that empties the list, then print it.
18. Join the lists `front_end = ['HTML','CSS','JS','React','Redux']` and `back_end = ['Node','Express','MongoDB']`. Print the joined list.
19. After joining, copy the joined list to `full_stack`, find the index of `'Redux'` and insert `'Python'` and `'SQL'` immediately after it. Print `full_stack`.
20. Given `ages = [19,22,19,24,20,25,26,24,25,24]`: sort the list, find and print the minimum and maximum ages.
21. Add a new minimum age (e.g., 16) at the beginning and a new maximum age (e.g., 56) at an appropriate position; then print the updated `ages` list.
22. Calculate and print the median age. If even number of elements, print the average of the two middle values.
23. Calculate and print the average age.
24. Using the `countries` list from `countries_list.py`, find and print the middle country (or countries if even length).
25. Divide the `countries` list into two halves. If the list has an odd number of countries, place the extra country in the first half. Print both halves.

## Bonus
- Explain what happens when you try to access an index that is out of range.
- Demonstrate copying a list vs referencing it (i.e., show `copy()` vs assignment) and explain the difference.
- Implement a small function `median(nums)` that returns the median for any numeric list and test it with `ages`.

---

Feel free to run `list_exercise.py` to see printed outputs, or open this markdown to use the exercises in a learning session.

## Full `list_exercise.py` source

```python
from countries_list import countries

# Exercise List

# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
shopping_list = ["Banana", "Apple", "Grapes", "Mango", "Melon", "Orange", "Guava"]
print(shopping_list)

# Find the length of your list
print(len(shopping_list))

# Get the first, middle and last item
print(shopping_list[0])
print(shopping_list[len(shopping_list)//2])
print(shopping_list[-1])

# Mixed data types
mixed_data_types = ["Muhammad Fayaz", 26, 168, "Single", "P22"]
print(mixed_data_types)

# IT companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'C', 'Amazon']

# Print the list
print(it_companies)

# Print number of companies
print(len(it_companies))

# Print first, middle and last company
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

# Modify one company
it_companies[0] = 'Quanrio'
print(it_companies)

# Add an IT company
it_companies.insert(1, 'IT')
print(it_companies)

# Insert company in middle
it_companies.insert(len(it_companies)//2, 'IT')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
upper_case= it_companies[0]=it_companies[0].upper()
print(upper_case)


# Join the it_companies with a string '#;  '

print('#; '.join(it_companies))
 

#Check if a certain company exists in the it_companies list.
print("Microsoft" in it_companies)


#Sort the list using sort() method
unsort_list=[4,5,23,6,42,0,7]
sort_list=sorted(unsort_list)
print(sort_list)

#Reverse the list in descending order using reverse() method
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)


#Slice out the first 3 companies from the list
print(it_companies[0:3])

#Slice out last first 3 companies from the list

print(it_companies[-3:])

#Slice out the middle IT company or companies from the list

mid = len(it_companies) // 2
print(it_companies[mid])

#Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)


#Remove the middle IT company or companies from the list
middle = len(it_companies) // 2
it_companies.pop(middle)
it_companies.pop(middle - 1)
print(it_companies)

#Remove the last IT company from the list
it_companies.pop()
print(it_companies)

#Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#Destroy the IT companies list

# it_companies2 = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'C', 'Amazon']
# del it_companies2
# print(it_companies2)


# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

print(front_end+back_end)

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

full_stack = front_end + back_end
# find Redux position
index = full_stack.index("Redux")

full_stack.insert(index + 1, "Python")
full_stack.insert(index + 2, "SQL")

print(full_stack)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
sort_ages= sorted(ages)
min_age=min(sort_ages)
max_age=max(sort_ages)
print(sort_ages)
print(min_age)
print(max_age)


#Add the min age and the max age again to the list
add_min=ages.insert(0,16)
add_max=ages.insert(4,56)

print(ages)


#Find the median age (one middle item or two middle items divided by two)
ages.sort()

n = len(ages)
mid = n // 2

if n % 2 == 0:
	median = (ages[mid - 1] + ages[mid]) / 2
else:
	median = ages[mid]

print("Median age:", median)


#Find the average age (sum of all items divided by their number )
avg_age= sum(ages)/len(ages)
print(avg_age)


#Find the middle country(ies) in the countries list

middle_country=len(countries)//2
print(countries[mid])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.

devide_countiry= len(countries)/2

```

## Sample run output

```
(See the script run output captured when executed in your workspace.)

