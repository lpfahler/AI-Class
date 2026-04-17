# AI on the Edge - Lesson 3
# Class Code - Grades Program
# Lori Pfahler
# April 2026

while True:
    # get number of grades from user and create a list to hold them
    num_grades = int(input('\nHow many grades? '))
    grades = []
    # get the grades from the user
    for i in range(num_grades):
        grade = int(input('Enter grade ' + str(i + 1) + ': '))
        grades.append(grade)
    # print out the entered grades
    print('\nYou entered the following grades:')
    for i in range(num_grades):
        print('Grade ', i + 1, ': ', grades[i], sep = '')
        