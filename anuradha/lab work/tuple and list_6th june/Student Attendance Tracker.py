attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

# Count present and absent days
present = 0
absent = 0

for day in attendance:
    if day == 'P':
        present += 1
    else:
        absent += 1

print("Present Days:", present)
print("Absent Days:", absent)

# Attendance percentage
percentage = (present / len(attendance)) * 100

print("\nAttendance Percentage:", percentage)

# Eligibility
if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")

# Absent positions
print("\nAbsent Positions:")

for i in range(len(attendance)):
    if attendance[i] == 'A':
        print(i + 1)