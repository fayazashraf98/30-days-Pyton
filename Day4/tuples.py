# Tuples
# A tuple is an ordered, immutable collection. Once created, its items cannot be changed.
# Tuples do not support methods that modify content (like add, insert, remove).

# Empty tuple literal and its type
print(())
print(type(()))

# Create an empty tuple using the constructor and show its type
t = tuple()
print(t)
print(type(t))


# Example tuple of years (tuples can contain duplicates)
years = (2012, 2015, 2016, 2016, 2016, 2020, 2021, 2022)

# Indexing: first and last element
print(years[0])   # first element
print(years[-1])  # last element

# Count occurrences of a value and membership test
print(f"How many times 2016 occurs: {years.count(2016)}")
print(2023 in years)  # membership test -> False

# Example: difference from a start year for each element
start_year = 2010
for year in years:
    # .count() returns how many times `year` appears in the tuple
    # .index() returns the index of the first occurrence
    print(f"Year: {year}, count: {years.count(year)}, first_index: {years.index(year)}")
    print("Years since start:", year - start_year)


# Concatenation of tuples produces a new tuple (tuples are immutable)
tp1 = (1, 2, 3)
tp2 = (4, 5, 6)
print(tp1 + tp2)


# Tuples of country names
# Corrected variable names to `countries` for clarity
nordic_countries = ('Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland')
print(nordic_countries)

# Slicing returns a new tuple (or subsequence)
scandinavian_countries = nordic_countries[1:]
print(scandinavian_countries)
print(nordic_countries[1:4])

# Convert a tuple to a list when you need a mutable sequence
print(list(nordic_countries))

