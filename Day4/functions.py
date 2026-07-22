

# What is funcitons?
# function is the set of cod that perform a certain task
# it may take an input and it returns an output
# we can reuse functions
# fucntion can be builtin funtion or custion fucntion



print('I love pyton', 2021, 'you can put anythong as an argument')
print('a','b','c')


# def is keyword that allow to create a fucntion

# A function with no parameters.
def name_of_func():
    print("i am a fucntion")

name_of_func()

# Another simple function example.
def do_something():
    print("i am doing something too ")

do_something()


# Function that takes one argument and prints its square.
def make_squre(n):
    print(n*n)

make_squre(3)
make_squre(4)
make_squre(12)
make_squre(8)
make_squre(34)


# Function that returns a calculated value instead of printing it.
def do_something_return(n):
    square = n ** 2
    return square
print(do_something_return(3))



# Function that adds two numbers and returns the result.
def add_two_nums(a,b):
    return a+b
print(add_two_nums(1,9))


# Function that combines a first name and last name.
def print_fullname(first_name, last_name):
    full_name = first_name+' '+last_name
    return full_name

print(print_fullname('Muhammad','Fayaz'))
print(print_fullname('Donald','Trump'))
print(print_fullname('Steve','Jobs'))


# Sum numbers from 0 to 100.
total= 0
for i in range(101):
    total=total+i
    print(total)


# Function that returns the sum of numbers from 0 to n.
    def sum_of_nums(n):
        total =0
        for i in range(n+1):
            total = total+i
        return total
    print(sum_of_nums(3))
    print(sum_of_nums(10))
    print(sum_of_nums(100))


    # Calculate weight using mass and gravity.
mass=75
gravity=9.81
weight= mass * gravity
print(weight)

    # Same calculation, but with a default gravity value.
def calculate_mess(mess,gravity=9.81):
    return round(mess * gravity,1)
print(calculate_mess(75))
print(calculate_mess(75,1.65))



    # Check whether a number is even or odd.
def check_num(n):
    if n % 2 == 0:
        return 'Even'
    return 'Odd'

print(check_num(3))


# Arbitrary or unlimited number of arguments
# if  we dont know the number of argumenbt we pas to the funtion 
# we can create a funtion which can take arbitrary number of argmuments by adding * befor the paramenter name.


# Add any number of values passed to the function.
def add_nums(*args):   # if you have * it changes to tuple
    total =0
    for i in args:
        total = total +i
    return total
print( add_nums(1,3,4,5))