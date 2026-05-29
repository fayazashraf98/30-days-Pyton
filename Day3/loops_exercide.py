from countries_list import countries


# # Exercises: Level 1


# # Iterate 0 to 10 using for loop, do the same using while loop.
# print("For Loop")
# for i in range(11):
#     print(i)

# print("While Loop")

# i=0
# while i<11:
#     print(i)
#     i=i+1


# # Iterate 10 to 0 using for loop, do the same using while loop.

# print("For Loop")
# for i in range(10,-1,-1):
#     print(i)

# print("While Loop")

# i=10
# while i>=0:
#     print(i)
#     i=i-1


# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######

# for i in range(7):
#     i=i+1
#     print('#'*i)


#Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()


# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100


for i in range(11):
    print(f'{i} x {i} = {i*i}')


#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

lst=['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst:
    print(i)

# Use for loop to iterate from 0 to 100 and print only even numbers

for i in range(1,100):
    if i%2==0:
        print(i)

#Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(1,100):
    if i%2!=0:
        print(i)

##Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum_of_num = 0
for i in range(101):
    print(i)
    sum_of_num = sum_of_num + i
print('The sum of all numbers is', sum_of_num)

##Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_of_even_num = 0
sum_of_odd_num = 0
for i in range(101):
    if i%2==0:
        sum_of_even_num = sum_of_even_num + i
    if i%2!=0:
        sum_of_odd_num = sum_of_odd_num + i
print(f'The sum of all evens is {sum_of_even_num}. And the sum of all odds is {sum_of_odd_num}')


for country in countries:
    if 'land' in country:
        print(country)