# String-Based Attendance Tracker

# Taking attendance input
attendance = input("Enter Attendance Record: ")

# Count present and absent
present_days = attendance.count("P")
absent_days = attendance.count("A")

# Total days
total_days = len(attendance)

# Calculate percentage
percentage = (present_days / total_days) * 100

# Variables for longest streak
max_present = 0
current_present = 0

max_absent = 0
current_absent = 0

# Find streaks
for ch in attendance:

    # Present streak
    if ch == "P":
        current_present += 1
        current_absent = 0

    # Absent streak
    else:
        current_absent += 1
        current_present = 0

    # Update max streak
    if current_present > max_present:
        max_present = current_present

    if current_absent > max_absent:
        max_absent = current_absent

# Display output
print("\nAttendance Record:")
print(attendance)

print("\nPresent Days:", present_days)
print("Absent Days:", absent_days)

print("\nAttendance Percentage:", round(percentage, 2), "%")

print("\nLongest Present Streak:", max_present)
print("Longest Absent Streak:", max_absent)

# Check attendance status
if percentage < 75:
    print("\nAttendance Status: Below 75%")
else:
    print("\nAttendance Status: Good Attendance")