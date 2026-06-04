present = 0
absent = 0

for student in range(1, 31):
    status = input(f"Student {student} Attendance (Present/Absent): ")

    if status.lower() == "present":
        present += 1
    else:
        absent += 1

print("\nNo. of Students Present:", present)
print("No. of Students Absent:", absent)