# AI on the Edge - Lesson 3
# Class Code
# Lori Pfahler
# April 2026

print('Hello World')
print('Hello Lori')

# variables - integers
x = 7
print(x)
y = 3
print(y)
z = x + y
print(z)

# variables - float
x = 2.0
print(x)

# mixing variable types in calculations
x = 7
y = 3.5
z = x + y
# z will be a float
print(z)
# division of integers will become a float
x = 7
y = 2
z = x/y
print(z)

# variables - strings - can use double or single quotes
my_fruit = 'banana'
my_fruit_2 = "apple"
print(my_fruit, my_fruit_2)
# use double quotes to deal with single quotes you want to print
my_text = "don't"
print(my_text)

# lists/arrays in python
# list of integers
my_list = [5, 4, 3, 2, 1]
print(my_list)

# indexing lists - print the second position in my_list
print(my_list[1])
# try to print an index not in array - get an error
# print(my_list[5])

# modify list
my_list[0] = 7
print(my_list)

# append to a list
my_list.append(0)
print(my_list)

# 2-dim array/list
# 1 0 0
# 0 1 0
# 0 0 1
my_array = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(my_array)
# address row and then column to get specific value row 1 col 1
print(my_array[1][1])

# 3-dim array - eg colors in RGB format 3 columns and two rows of RGB data
my_rgb = [[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
          [[0, 255, 255], [255, 0, 255], [0, 255, 255]]]
print(my_rgb)
# get first row second col RGB data
print(my_rgb[0][1])
# get first row, second col, green value
print(my_rgb[0][1][1])

# can use floats and strings in lists/arrays
my_fruits = ['apple', 'orange', 'banana']
print(my_fruits)
# can index characters inside the list
# get fourth character in 'orange'
print(my_fruits[1][3])

# watch how you handle strings vs variable names
msg = 'Hello World'
print('msg')
print(msg)

# simple print formatting
x = 7
y = 2
z = x + y
print('x + y =', z)
print(x, ' + ', y, ' = ', z)

# get input from user
grade1_str = input('What is your first grade? ')
print('Your first grade is:', grade1_str)
grade2_str = input('What is your second grade? ')
print('Your second grade is:', grade2_str)

# input returns strings
sum_str = grade1_str + grade2_str
print(grade1_str, ' +', grade2_str, ' = ', sum_str)

# fix so grade1 and grade2 are integers
grade1 = int(input('What is your first grade? '))
grade2 = int(input('What is your second grade? '))
print(grade1, ' + ', grade2, ' = ', grade1 + grade2)

# if you want a float
my_float = float(input('Enter a float: '))
print(my_float)

# conditionals
if my_float > 0:
    print('Your float is positive.')
elif my_float < 0:
    print('Your float is negative.')
else:
    print('Your float is zero.')
               





