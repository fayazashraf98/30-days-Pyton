import math


math.pi

# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

# def add_two_numbers(a,b):
#     total=a+b
#     return total
# print(add_two_numbers(4,5))

# # Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# def circle(r):
#    area= math.pi*r*r
#    return area
# print(circle(3))

# ##Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
 
# def add_all_nums(*args):
#     total=0
#     for i in args:
#         total=total+i
#     return total
# print( add_all_nums(1,3,4,5))

# ## Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

# def convert_celsius_to_fahrenheit(c):
#     f=(c*9/5)+32
#     return f
# print(convert_celsius_to_fahrenheit(3))

# # #Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

# def check_season(month):
#     month = month.capitalize()

#     if month in ['March', 'April', 'May']:
#         return 'Spring 🌸'
#     elif month in ['June', 'July', 'August']:
#         return 'Summer ☀️'
#     elif month in ['September', 'October', 'November']:
#         return 'Autumn 🍂'
#     elif month in ['December', 'January', 'February']:
#         return 'Winter ❄️'
#     return 'Invalid month'
# print(check_season('June'))

# # Write a function called calculate_slope which return the slope of a linear equation

# def calculate_slope(y1, y2, x1, x2):
#     m = (y2 - y1) / (x2 - x1)
#     return m

# print(calculate_slope(3, 2, 3, 1))


# # Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

# def solve_quadratic_eqn(x,a,b,c):
#     quadratic=a*x**2+b*x+c
#     return quadratic
# print(solve_quadratic_eqn(3,10,5,2))


# # #Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

# def print_list(list):
#     for i in list:
#         print(i)
# print_list([1,2,3,4])


# ## Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

# def reverse_list(lst):
#     rev_list=[]
#     for i in range(len(lst)-1,-1,-1):
#         rev_list.append(lst[i])
#     return rev_list
# print(reverse_list([1, 2, 3, 4, 5]))
# print(reverse_list(["A", "B", "C"])) 

# ## Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# def capitalize_list_items(lst):
#     for i in lst:
#         print(i.capitalize())
# capitalize_list_items(['a','b','c'])

# # Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# # food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# # print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# # numbers = [2, 3, 7, 9];
# # print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# numbers = [2, 3, 7, 9];
# def add_item(lst,items):
#     lst.append(items)
#     return lst
# print(add_item(numbers,4))
# print(add_item(food_stuff, 'Meat'))


# # Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# # food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
# # print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# # numbers = [2, 3, 7, 9]
# # print(remove_item(numbers, 3))  # [2, 7, 9]

# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# numbers = [2, 3, 7, 9];
# def remove_item(lst,items):
#     lst.remove(items)
#     return lst
# print(remove_item(numbers,2))
# print(remove_item(food_stuff, 'Potato'))



# # Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# # print(sum_of_numbers(5))  # 15
# # print(sum_of_numbers(10)) # 55
# # print(sum_of_numbers(100)) # 5050

# def sum_of_numbers(num):
#     total =0
#     for i in range(1,num+1):
#         total +=i
#     return total
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050s


# # Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

# def sum_of_odds(n):
#     total = 0
#     for i in range(1, n + 1):
#         if i % 2 != 0:
#             total += i
#     return total

# print(sum_of_odds(5))  # 9 (1 + 3 + 5)


# # Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
# def sum_of_odds(n):
#     total = 0
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             total += i
#     return total

# print(sum_of_odds(5))  # 9 (1 + 3 + 5)


# ## Exercises: Level 2

# ## Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
# #     print(evens_and_odds(100))
# #     # The number of odds are 50.
# #     # The number of evens are 51.



def evens_and_odds(num):
    total_odd = 0
    total_even = 0

    for i in range(num + 1):
        if i % 2 != 0:
            total_odd += 1
        else:
            total_even += 1

    print(f"The number of odds are {total_odd}.")
    print(f"The number of evens are {total_even}.")

evens_and_odds(100)


##Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
   if num>0:
    print(f"The Factorial of {num} is : {math.factorial(num)}")
   else:
    print("Factorial is not defined for negative numbers")

factorial(6)


## Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(value):
    if value == "" or value == [] or value == {} or value is None:
        print("it empty")
    else:
        print("You entered:", value)

is_empty("")


# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range,
#  calculate_variance, calculate_std (standard deviation).


# def calculate_mean(lst):
#     total=0
    
#     for i in lst:
#       total+=i

#     mean=total/len(lst)
#     return mean
# print(calculate_mean([1,2,3,4,5]))

def calculate_median(lst):
    lst.sort()
    n = len(lst)

    if n % 2 != 0:
        median = lst[n // 2]
    else:
        mid1 = lst[n // 2 - 1]
        mid2 = lst[n // 2]
        median = (mid1 + mid2) / 2

    print(f"The Median is: {median}")


calculate_median([1, 2, 3, 4])


def calculate_mode(l, h, fm, f1, f2):
    numerator = fm - f1
    denominator = (2 * fm) - f1 - f2

    if denominator == 0:
        return "Mode is undefined (division by zero)"

    mode = l + (numerator / denominator) * h
    return mode

print(calculate_mode(12, 2, 4, 6, 7))



def calculate_range(lst):
    cal_range=max(lst)-min(lst)
    print(cal_range)

calculate_range([77,89,92,64,78,95,82])



#Write a function called greet which takes a default argument, name. 
# If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.


def greet(name="Guest"):
    if not name.strip():
        return "Hello, Guest!"
    return f"Hello, {name}!"

print(greet())
print(greet(""))
print(greet("Fayaz"))
        

   

# Create a function called show_args to take an arbitrary number of named arguments and print their names and values.


def show_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
show_args(name="Alice", age=30, city="New York")


# Exercises: Level 3



# Write a function called is_prime, which checks if a number is prime.


def is_prime(num):
    if num%2==0:
        return 'Prime'
    else:
        return 'Not Prime'
print(is_prime(1))


# Write a functions which checks if all items are unique in the list.

def is_unique(items):
    return len(items) == len(set(items))

print(is_unique([1,2,3,4,5,5]))



#Write a function which checks if all the items of the list are of the same data type.


def same_datatype(items):
    if not items:
        return True
    return all(type(item) == type(items[0]) for item in items)

print(same_datatype([1, 2, 3, 4]))