quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# Students scoring 15 or above
print("Students scoring 15 or above:")

for student in quiz_scores:
    if quiz_scores[student] >= 15:
        print(student, quiz_scores[student])

# Students scoring below 10
count = 0

for student in quiz_scores:
    if quiz_scores[student] < 10:
        count += 1

print("\nStudents scoring below 10:", count)

# Top performer
highest = max(quiz_scores, key=quiz_scores.get)

print("\nTop Performer:")
print(highest, quiz_scores[highest])

# Passed students
passed = []

for student in quiz_scores:
    if quiz_scores[student] >= 10:
        passed.append(student)

print("\nPassed Students:")
print(passed)

# Class average
total = 0

for student in quiz_scores:
    total += quiz_scores[student]

average = total / len(quiz_scores)

print("\nClass Average:", average)