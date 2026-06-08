# Dictionary storing employee performance scores
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# Display employees scoring above 80
print("Employees Scoring Above 80:")

for emp in performance:
    if performance[emp] > 80:
        print(emp)

# Count employees needing improvement
count = 0

for emp in performance:
    if performance[emp] < 60:
        count += 1

print("\nEmployees Needing Improvement:", count)

# Find top performer
top_employee = ""
highest_score = 0

for emp in performance:
    if performance[emp] > highest_score:
        highest_score = performance[emp]
        top_employee = emp

print("Top Performer:", top_employee, "(", highest_score, ")", sep="")

# Calculate average performance score
total = 0

for emp in performance:
    total += performance[emp]

average = total / len(performance)

print("Average Score:", average)

# Create separate lists
excellent = []
good = []
average_list = []
poor = []

for emp in performance:
    score = performance[emp]

    if score >= 90:
        excellent.append(emp)

    elif score >= 75:
        good.append(emp)

    elif score >= 60:
        average_list.append(emp)

    else:
        poor.append(emp)

print("Excellent:", excellent)
print("Good:", good)
print("Average:", average_list)
print("Poor:", poor)