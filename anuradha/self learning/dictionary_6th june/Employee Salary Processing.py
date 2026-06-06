salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# Employees earning above 60000
print("Employees earning above ₹60,000:")

for emp in salary:
    if salary[emp] > 60000:
        print(emp, salary[emp])

# Employees earning below 40000
count = 0

for emp in salary:
    if salary[emp] < 40000:
        count += 1

print("\nEmployees earning below ₹40,000:", count)

# Highest paid employee
highest = max(salary, key=salary.get)

print("\nHighest Paid Employee:")
print(highest, salary[highest])

# Bonus list
bonus = []

for emp in salary:
    if salary[emp] > 50000:
        bonus.append(emp)

print("\nEmployees eligible for bonus:")
print(bonus)

# Average salary
total = 0

for emp in salary:
    total += salary[emp]

average = total / len(salary)

print("\nAverage Salary:", average)