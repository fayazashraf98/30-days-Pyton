"""
Higher-order function: a function that either takes another function as an argument,
or returns a function as its result.

When it is used:
- when you want to pass behavior into a function instead of hard-coding it
- when you want to build reusable, flexible, and shorter code
- when you want to apply the same logic to different functions
"""

# This function is a simple example that returns a squared value.
def make_squre(n):
    return n ** 2

# Call the function and multiply the result.
print(make_squre(2)* 2)


# This higher-order function receives another function as input.
# It calls that function and then multiplies the result.
def make_cube(func,n):
    return func(n) * n

print(make_cube(make_squre,2))


# This function uses a nested function to show that functions can be created inside functions.
def do_some_math(n):
    def add_ten():
        return n+10
    return add_ten()

# The nested function is called through the outer function.
print(do_some_math(5))
print(do_some_math(100))