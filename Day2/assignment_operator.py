a=5

# Assignment operators in Python
# Assignment operators store values in variables and can combine
# an operation with assignment (shorthand forms).

a = 5
print("Initial a:", a)

# Basic assignment
count = 0
print('\nBasic assignment:')
print(f"  count = {count}")

# Increment using long form and shorthand
print('\nIncrement examples:')
count = count + 1      # long form: add and assign
print(f"  after 'count = count + 1' -> {count}")
count += 1             # shorthand (add then assign)
print(f"  after 'count += 1' -> {count}")

# Other compound assignment operators
print('\nCompound assignment operators:')
value = 10
print(f"  start value = {value}")
value -= 2             # subtract and assign
print(f"  value -= 2 -> {value}")
value *= 3             # multiply and assign
print(f"  value *= 3 -> {value}")
value /= 4             # divide and assign (result may be float)
print(f"  value /= 4 -> {value}")
value %= 3             # modulus and assign
print(f"  value %= 3 -> {value}")
value **= 2            # exponent and assign
print(f"  value **= 2 -> {value}")
value //= 2            # floor divide and assign
print(f"  value //= 2 -> {value}")

# Notes:
# - Use compound assignment to write concise, idiomatic code.
# - Be mindful of types: '/=' produces floats, while '//=' uses floor division.
