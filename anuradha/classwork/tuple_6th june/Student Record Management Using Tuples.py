students = (
    (101, "Rahul", "Python", 25000),
    (102, "Priya", "Java", 30000),
    (103, "Amit", "Data Science", 45000),
    (104, "Sneha", "Python", 25000),
    (105, "Rohan", "MERN", 40000)
)

# 1. Display all student records
print("All Student Records:")

for student in students:
    print(student)

# 2. Display first student's details
print("\nFirst Student Details:")
print(students[0])

# 3. Display last student's details using negative indexing
print("\nLast Student Details:")
print(students[-1])

# 4. Display only Student ID and Name
print("\nStudent ID and Name:")

for student in students:
    print("ID:", student[0], "Name:", student[1])

# 5. Count total number of students
print("\nTotal Number of Students:")
print(len(students))

# 6. Check whether Rahul exists
found = False

for student in students:
    if student[1] == "Rahul":
        found = True
        break

if found:
    print("\nRahul exists in the records")
else:
    print("\nRahul does not exist in the records")