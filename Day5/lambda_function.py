
# Normal function example


def greet_people(name):
    # This function prints a greeting for one person.
    print("Hi", name)

greet_people("Jawad")
greet_people("Agha")
greet_people("Hadi")
greet_people("Fayaz")

# Reuse the same function with a loop.
for name in ['Fayaz','jawad','Agha','Hadi']:
    greet_people(name)


# Lambda function: a function without a name (anonymous function).
# It is useful for short, one-line operations.

# Both are same funtions:
def make_square(x):
    return x ** 2
print(make_square(2))

# The lambda version does the same thing in one line.
make_square = lambda x: x ** 2
print(make_square(2))

# A lambda can also accept multiple arguments.
make_diff_square = lambda x, y, z: x**2 + 2 * y + z
print(make_diff_square(2, 3, 4))