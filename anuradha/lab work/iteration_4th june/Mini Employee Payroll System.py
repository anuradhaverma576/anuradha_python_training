# Mini Employee Payroll System

# Input employee details
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: ₹"))

# Calculate salary components
hra = basic_salary * 0.20
da = basic_salary * 0.10
pf = basic_salary * 0.12

# Calculate gross and net salary
gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf

# Determine employee grade
if net_salary > 50000:
    grade = "Senior Grade"
elif net_salary > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"

# Display result
print("\n----- Employee Payroll System -----")
print("Employee Name:", name)
print("Basic Salary: ₹", basic_salary)
print("HRA (20%): ₹", hra)
print("DA (10%): ₹", da)
print("PF Deduction (12%): ₹", pf)
print("Gross Salary: ₹", gross_salary)
print("Net Salary: ₹", net_salary)
print("Employee Grade:", grade)