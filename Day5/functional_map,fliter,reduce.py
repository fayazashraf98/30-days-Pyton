"""
Map, filter, reduce

Map: transforms every item in an iterable one by one.
Filter: keeps only the items that pass a condition.
Reduce: combines all items into a single result.

Why use them?
- to write shorter and clearer code
- to apply the same operation to many values
- to separate transformation, filtering, and aggregation logic
"""

# Map example: transform each country name to uppercase.
print([c.upper() for c in ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']])

# Filter example: keep only values that match a condition.
"""
For numbers:
[0, 1, 2, 3, 4] -> even numbers -> [0, 2, 4]
[0, 1, 2, 3, 4] -> odd numbers -> [1, 3]
"""

# Traditional method: build a new list with a loop.
"""
nums = [0, 1, 2, 3, 4]
new_lst = []
for num in nums:
    new_lst.append(num ** 2)
print(new_lst)
"""

# Map method: apply the same operation to every number.
nums=[0,1,2,3,4]
new_lst=list(map(lambda x:x ** 2, nums))
print(new_lst)


 # Traditional method: convert each country name with a loop.
"""
coutries=['Finland', 'Sweden', 'Norway','Denmark','Iceland']
new_lst_country=[]
for c in coutries:
    new_lst_country.append(c.upper())
print(new_lst_country)"""

# Map method: transform each country name to uppercase.

coutries=['Finland', 'Sweden', 'Norway','Denmark','Iceland']
new_country_lst=list(map(lambda country: country.upper(),coutries))
print(new_country_lst)



# Traditional method: filter even numbers with a loop.

"""
ev_nums=[0,1,2,3,4]
evens=[]
for num in ev_nums:
    if num % 2 == 0:
        evens.append(num)
print(evens)
"""
# Filter method: keep only the even numbers.
ev_nums=[0,1,2,3,4]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)


# Filter method: keep only countries that contain 'land'.

coutries=['Finland', 'Sweden', 'Norway','Denmark','Iceland']
countires_with_land = list(filter(lambda country: 'land' in country, coutries))
print(countires_with_land)





from functools import reduce
nums= [0,1,2,3,4]

# Reduce method: combine all values into one result.
print(reduce(lambda x, y: x + y, nums))
