marks = [78, 45, 92, 35, 88, 40, 99, 56]

passed = []
failed_count = 0
merit_list = []

highest = marks[0]
lowest = marks[0]

for mark in marks:
    # Passed students
    if mark >= 40:
        passed.append(mark)
    else:
        failed_count += 1

    # Highest marks
    if mark > highest:
        highest = mark

    # Lowest marks
    if mark < lowest:
        lowest = mark

    # Merit list
    if mark > 75:
        merit_list.append(mark)

print("Passed Students:", passed)
print("Failed Count:", failed_count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit_list)