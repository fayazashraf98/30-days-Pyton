import math

# # Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

# base=float( input("Enter the Base: "));
# height =float (input("Enter the height : "));
# area=0.5* base * height
# print("The Area of triangle is:", area)


# # # Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# print('\n')
# side_a = int (input("Enter the side a :"))
# side_b= int (input("Enter the side b :"))
# side_c = int (input("Enter the side c :"))
# perimeter= side_a+side_b+side_c
# print("The perimeter is :",perimeter)

# # Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

# length= float(input("Enter the length: "))
# width= float(input("Enter the width: "))
# area= length * width
# perimeter= 2*(length+width)
# print("Area = ",area)
# print("perimeter = ",perimeter)


# # Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

# pi= 3.14
# r=float(input ("Enter the r: "))
# area =pi * r * r
# print("Area = ",round(area,2))
# circumference = 2 * pi *r
# print("circumference = ",circumference)


# # Calculate the slope, x-intercept and y-intercept of y = 2x -2

# slope = 2
# y_intercept = -2
# x_intercept = 1

# print("Slope =", slope)
# print("Y-Intercept =", y_intercept)
# print("X-Intercept =", x_intercept)



# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

# x1 = 2
# y1 = 2
# x2 = 6
# y2 = 10
# slope =(y2-y1)/(x2-x1) #Slope Formula 
# print("The Slope is : ",slope)
# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# print("Euclidean Distance is:", round(distance,2))


# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.


# value_x = int (input("Enter the  x value :"))
# value_y = value_x**2 + 6*value_x + 9
# print(value_y)

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.

# print('The Length of "Python" :',len('python'))
# print('The Length of "dragon" :',len('dragon'))
# print('Is length of python equal to dragon?:', len('python') == len('dragon'))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'

# word1='python'
# word2='dragon'
# print('on' in word1 and 'on' in word2)


# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

# sentence = "I hope this course is not full of jargon"
# print("jargon" in sentence)


#There is no 'on' in both dragon and python

# py='python'
# dr='dragon'
# print('on' not in py and 'on' not in dr)

# Find the length of the text python and convert the value to float and convert it to string
# text1="python"
# print(len(text1))
# print(float(len(text1)))
# print(str(len(text1)))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

# num1= 2
# check_num= num1%2
# if num1%2 ==0:
#     print("Even")
# else:
#     print("odd")



#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

# flor_div=7//3
# con_val = int(2.7)
# print(flor_div)
# print(flor_div==con_val)


#Check if type of '10' is equal to type of 10

# type1 = '10'
# type2 = 10

# print(type(type1) == type(type2))


# Check if int('9.8') is equal to 10

# num1 = int(float('9.8'))
# print(num1 == 10)


# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

# hours= int(input("Enter hours: "))
# rate_per_hour= int(input("Enter rate per hour:"))
# pay= hours * rate_per_hour
# print("Your Weekly Earning is : ",pay)





# Write a script that prompts the user to eyears. Calculate the number of seconds a person can live. Assume a person can live hundred years

# ageYears= int(input("number of years you have lived: "))
# seconds = ageYears * (365*24*60*60)
# print(seconds)










