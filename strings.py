course = "Python's Course for Beginners"  # double quotes used when single quote in string
course2 = "Python for \"Beginners\""  # can escape with \
print(course2)

course3 = '''
Hi Blair,

This is our first email to you.

Thank you.
'''
print(course3)

course4 = 'Python for Beginners'
print(course4[0])  # print character at index of 0
print(course4[-1])  # negative index start from the end of the string
print(course4[0:3])  # return from 0 to 2
print(course4[3:])  # return all starting from index
print(course4[:5])  # assumes 0 as start index

another = course[:]  # copy string to another variable
print(another)

name = 'Jennifer'
print(name[1:-1])

first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'  # formatted string
print(message)
print(msg)

