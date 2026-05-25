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

# extend : to add the multiple items inside the list
it_companies.extend(['Quaniro', 'GMS', "Jazz"])
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






























