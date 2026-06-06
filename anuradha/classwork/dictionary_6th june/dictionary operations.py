# to create a dictionary to store student's data
students = {
    'std101': "Akash",
    'std102': "Abhinav",
    'std103': "Anil",
    'std104': 'Rahul'
}

# display the data
print("Student details : ")
print(students)

print("-----------------------------------")

# update record of student whose roll number is std103
students['std103'] = 'Rohit'

# add a new student std105
students['std105'] = 'Rakesh'

print("Student details : ")
print(students)

print("-----------------------------------")

# display all students one by one
for x in students:
    print(x, ' -> ', students[x])