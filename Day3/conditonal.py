

#----------------------------------------------------------------------------------------------------------------------

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive.
#  If below 18 give feedback to wait for the missing amount of years. Output:

age = int (input("Enter you age: "))
currecnt_age= 18- age

if age > 18 or age == 18:
    print("You are old enough to learn to drive.")
elif age <0:
    print("Invalid age")
else:
    print(f"You need {currecnt_age} more years to learn to drive.")
    


#----------------------------------------------------------------------------------------------------------------------
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) 
# to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, 
# and a custom text if my_age = your_age. Output:

my_age= int (input("Enter my age: "))
your_age= int(input("Enter your age: "))
diff_age = abs(my_age - your_age)
if my_age>your_age:
    print(f"you are {diff_age} years older than me.")
elif my_age==your_age:
    print(f"we both have a same age")
else:
    print(f"you are {diff_age} years elder than me.")

#----------------------------------------------------------------------------------------------------------------------
# Get two numbers from the user using input prompt.
#  If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

a=int(input("Enter a: "))
b= int (input ("Enter b:"))
if a>b:
    print(f"{a} is greater than {b}")
elif a==b:
    print(f"{a} is equl to {b}")
else:
    print(f"{a} is smaller than {b}")


#----------------------------------------------------------------------------------------------------------------------

# Write a code which gives grade to students according to theirs scores:
# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F

score=float(input("Enter you score: "))
score = float(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid input")
elif score <= 59:
    print("F")
elif score <= 69:
    print("D")
elif score <= 79:
    print("C")
elif score <= 89:
    print("B")
else:
    print("A")



#----------------------------------------------------------------------------------------------------------------------

#Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn.
#  December, January or February, the season is Winter. 
# March, April or May, the season is Spring
#  June, July or August, the season is Summer

month = input("Enter the Month: ")
if month in ["September", "October", "November"]:
    print("Autumn")
elif month in ["December", "January", "February"]:
    print("Winter")
elif month in ["March", "April", "May"]:
    print("Spring")
elif month in ["June", "July", "August"]:
    print("Summer")
else:
    print("Invalid input")


#----------------------------------------------------------------------------------------------------------------------

# The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exist in the list')

find_fruit = input("Enter the fruit: ")
fruits = ['banana', 'orange', 'mango', 'lemon']
if find_fruit in fruits:
    print(f"{find_fruit} already exists in the list")
else:
    fruits.append(find_fruit)
    print(f"New item added to the list: {fruits}")


#----------------------------------------------------------------------------------------------------------------------

# Here we have a person dictionary. Feel free to modify it!

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'),
#       if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
#       if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
#       else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    skills=person['skills']
    middle= len(skills)//2
    print(skills[middle])


if 'skills' in person:
    skills=person['skills']
    if 'Python' in skills:
        print("Python is in the list")
    else:
        print("not in the list")

if 'skills' in person:
    skills = person['skills']

    if 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')

    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')

    elif 'JavaScript' in skills and 'React' in skills:
        print('He is a front end developer')

    else:
        print('unknown title')


if person['is_married'] == True and person['country'] == 'Finland':
    print(f"{person['first_name']} lives in {person['country']}. He is married")






