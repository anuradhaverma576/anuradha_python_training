employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# Employees earning above 50000
print("Employees earning above ₹50,000:")

for emp in employees:
    if emp[1] > 50000:
        print(emp[0], emp[1])

# Highest-paid employee
highest = employees[0]

for emp in employees:
    if emp[1] > highest[1]:
        highest = emp

print("\nHighest Paid Employee:")
print(highest[0], highest[1])

# Total salary expenditure
total = 0

for emp in employees:
    total += emp[1]

print("\nTotal Salary Expenditure:", total)

# Count employees below 40000
count = 0

for emp in employees:
    if emp[1] < 40000:
        count += 1

print("\nEmployees earning below ₹40,000:", count)