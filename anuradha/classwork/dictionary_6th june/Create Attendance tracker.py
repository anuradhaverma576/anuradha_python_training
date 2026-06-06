# Create an empty dictionary
attendance = {}

# Input attendance for 30 students
for i in range(30):
    roll_no = input("Enter Roll Number: ")
    status = input("Enter Attendance (Present/Absent): ")

    # Store data in dictionary
    attendance[roll_no] = status

print("\nAttendance Record:")
print(attendance)

# Display roll numbers of present students
print("\nStudents who are Present:")

for roll_no in attendance:
    if attendance[roll_no].lower() == "present":
        print(roll_no)