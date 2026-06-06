marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# Students scoring 80 or above
print("Students scoring 80 or above:")
for name in marks:
    if marks[name] >= 80:
        print(name, marks[name])

# Failed students
fail = 0
for name in marks:
    if marks[name] < 40:
        fail += 1

print("\nFailed Students:", fail)

# Highest scorer
highest = max(marks, key=marks.get)

print("\nHighest Scorer:")
print(highest, marks[highest])

# Students scoring between 60 and 75
students = []

for name in marks:
    if 60 <= marks[name] <= 75:
        students.append(name)

print("\nStudents scoring between 60 and 75:")
print(students)

# Grades
print("\nGrades:")

for name in marks:
    score = marks[name]

    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(name, "->", grade)