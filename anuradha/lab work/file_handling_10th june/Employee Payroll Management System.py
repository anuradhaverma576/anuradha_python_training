# Employee Payroll Management System


# Function to read employee data from file
def read_employees():

    employees = []

    file = open("employees.txt", "r")

    for line in file:
        data = line.strip().split(",")

        emp = {
            "id": data[0],
            "name": data[1],
            "salary": int(data[2])
        }

        employees.append(emp)

    file.close()

    return employees


# Function to display all employee records
def display_employees():

    employees = read_employees()

    print("\nEmployee Records")
    print("-" * 40)

    for emp in employees:
        print(emp["id"], emp["name"], emp["salary"])


# Function to search employee by ID
def search_employee():

    emp_id = input("Enter Employee ID: ")

    employees = read_employees()

    found = False

    for emp in employees:

        if emp["id"] == emp_id:
            print("\nEmployee Found")
            print("ID:", emp["id"])
            print("Name:", emp["name"])
            print("Salary:", emp["salary"])

            found = True
            break

    if found == False:
        print("Employee Not Found")


# Function to calculate average salary
def average_salary():

    employees = read_employees()

    total = 0

    for emp in employees:
        total += emp["salary"]

    average = total / len(employees)

    print("Average Salary =", average)


# Function to find highest and lowest paid employee
def highest_lowest_salary():

    employees = read_employees()

    highest = employees[0]
    lowest = employees[0]

    for emp in employees:

        if emp["salary"] > highest["salary"]:
            highest = emp

        if emp["salary"] < lowest["salary"]:
            lowest = emp

    print("\nHighest Paid Employee")
    print(highest["name"], "-", highest["salary"])

    print("\nLowest Paid Employee")
    print(lowest["name"], "-", lowest["salary"])


# Function to display employees earning above 50000
def employees_above_50000():

    employees = read_employees()

    print("\nEmployees Earning Above ₹50,000")
    print("-" * 40)

    for emp in employees:

        if emp["salary"] > 50000:
            print(emp["name"], "-", emp["salary"])


# Function to add new employee
def add_employee():

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Salary: ")

    file = open("employees.txt", "a")

    file.write("\n" + emp_id + "," + name + "," + salary)

    file.close()

    print("Employee Added Successfully")


# Function to generate salary categories
def salary_categories():

    employees = read_employees()

    print("\nSalary Categories")
    print("-" * 30)

    for emp in employees:

        salary = emp["salary"]

        if salary >= 60000:
            category = "High"

        elif salary >= 40000:
            category = "Medium"

        else:
            category = "Low"

        print(emp["name"], "->", category)


# Main Menu
while True:

    print("\n===== Employee Payroll Menu =====")
    print("1. Display All Employees")
    print("2. Search Employee by ID")
    print("3. Calculate Average Salary")
    print("4. Highest and Lowest Paid Employee")
    print("5. Employees Earning Above ₹50,000")
    print("6. Add New Employee")
    print("7. Salary Categories")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_employees()

    elif choice == "2":
        search_employee()

    elif choice == "3":
        average_salary()

    elif choice == "4":
        highest_lowest_salary()

    elif choice == "5":
        employees_above_50000()

    elif choice == "6":
        add_employee()

    elif choice == "7":
        salary_categories()

    elif choice == "8":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")