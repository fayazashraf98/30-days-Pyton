# Loops: repetition examples (for and while)
# This file demonstrates several common loop patterns with explanatory comments.

# iteration from 0 to 10 (inclusive)
# `range(11)` generates numbers 0..10
for i in range(11):
    # print the current loop variable
    print(i)


# Define a list of country names (corrected variable name)
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

# Build a new list of country info: [original, uppercase, first3-uppercase]
country_info = []
for country in countries:
    # append a small summary list for each country
    country_info.append([country, country.upper(), country.upper()[:3]])

# Print the list of country summaries
print(country_info)
# Example element: ['Finland', 'FINLAND', 'FIN']


# Print numbers from 0 to 100 (inclusive)
for num in range(101):
    print(num)


# Print numbers from 0 to 100 stepping by 10: 0, 10, ..., 100
for num in range(0, 101, 10):
    print(num)


# Find countries that contain the substring 'land'
# (case-sensitive check; names above contain 'land' in Finland/Iceland)
countries_with_land = []
for c in countries:
    if 'land' in c:
        # add matching country to the result list
        countries_with_land.append(c)
print(countries_with_land)


# Find countries that do NOT contain the substring 'land'
countries_without_land = []
for c in countries:
    if 'land' not in c:
        countries_without_land.append(c)
print(countries_without_land)


# Find countries that contain the substring 'way' (e.g., 'Norway')
countries_with_way = []
for c in countries:
    if 'way' in c:
        countries_with_way.append(c)
print(countries_with_way)


# Sum a list of numbers manually using a loop
nums = [0, 1, 2, 3, 4, 5, 6]
total = 0
for n in nums:
    # accumulate each number into total
    total += n
print(total)  # prints the sum: 21


# Collect even numbers from `nums` into a new list
evens = []
for n in nums:
    # check if the number is divisible by 2
    if n % 2 == 0:
        evens.append(n)
print(evens)


# Print squares for numbers 1..10
for t in range(1, 11):
    # format: "n x n = square"
    print(f'{t} x {t} = {t * t}')


# Demonstrate `continue`: skip negative numbers and keep printing others
random_nums = [0, 1, 2, 3, -7, 4, 5]
for x in random_nums:
    if x < 0:
        # skip this iteration when x is negative
        continue
    print(x)


# Demonstrate `break`: stop the loop when a negative number is encountered
random_nums = [0, 1, 2, 3, -7, 4, 5]
for x in random_nums:
    if x < 0:
        # exit the loop entirely when x is negative
        break
    print(x)


# Count down from 4 to 0 using a reversed range (step = -1)
for i in range(4, -1, -1):
    print(i)


# While loop example: repeat until condition is false
count = 0
while count < 5:
    # print the current counter and increment
    print('while loop count:', count)
    count += 1
