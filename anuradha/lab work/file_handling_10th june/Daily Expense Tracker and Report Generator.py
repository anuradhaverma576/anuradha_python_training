# Daily Expense Tracker and Report Generator


# Function to read expenses from file
def read_expenses():

    expenses = []

    file = open("expenses.txt", "r")

    for line in file:

        data = line.strip().split(",")

        expense = {
            "category": data[0],
            "amount": int(data[1])
        }

        expenses.append(expense)

    file.close()

    return expenses


# Function to update file
def update_file(expenses):

    file = open("expenses.txt", "w")

    for expense in expenses:

        line = (
            expense["category"] + "," +
            str(expense["amount"]) + "\n"
        )

        file.write(line)

    file.close()


# Function to display all expenses
def display_expenses():

    expenses = read_expenses()

    print("\nExpense Records")
    print("-" * 35)

    for expense in expenses:
        print(expense["category"],
              "- ₹",
              expense["amount"])


# Function to calculate total expenditure
def total_expenditure():

    expenses = read_expenses()

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expenditure = ₹", total)


# Function to find highest and lowest expense
def highest_lowest_expense():

    expenses = read_expenses()

    highest = expenses[0]
    lowest = expenses[0]

    for expense in expenses:

        if expense["amount"] > highest["amount"]:
            highest = expense

        if expense["amount"] < lowest["amount"]:
            lowest = expense

    print("\nHighest Expense")
    print(highest["category"],
          "- ₹",
          highest["amount"])

    print("\nLowest Expense")
    print(lowest["category"],
          "- ₹",
          lowest["amount"])


# Function to display expenses above ₹800
def expenses_above_800():

    expenses = read_expenses()

    print("\nExpenses Greater Than ₹800")
    print("-" * 35)

    for expense in expenses:

        if expense["amount"] > 800:
            print(expense["category"],
                  "- ₹",
                  expense["amount"])


# Function to add new expense category
def add_expense():

    category = input("Enter Category Name: ")
    amount = input("Enter Expense Amount: ")

    file = open("expenses.txt", "a")

    file.write("\n" + category + "," + amount)

    file.close()

    print("Expense Added Successfully")


# Function to update expense amount
def update_expense():

    category = input("Enter Category Name: ")

    expenses = read_expenses()

    found = False

    for expense in expenses:

        if expense["category"].lower() == category.lower():

            new_amount = int(input("Enter New Amount: "))

            expense["amount"] = new_amount

            update_file(expenses)

            print("Expense Updated Successfully")

            found = True
            break

    if found == False:
        print("Category Not Found")


# Function to generate report
def generate_report():

    expenses = read_expenses()

    total = 0

    highest = expenses[0]
    lowest = expenses[0]

    high_expenses = []

    for expense in expenses:

        total += expense["amount"]

        if expense["amount"] > highest["amount"]:
            highest = expense

        if expense["amount"] < lowest["amount"]:
            lowest = expense

        if expense["amount"] > 800:
            high_expenses.append(expense["category"])

    # Write report into file
    file = open("report.txt", "w")

    file.write("Expense Summary Report\n")
    file.write("-" * 30 + "\n")

    file.write("Total Expenses: ₹" +
               str(total) + "\n")

    file.write("Highest Expense Category: " +
               highest["category"] + "\n")

    file.write("Lowest Expense Category: " +
               lowest["category"] + "\n")

    file.write("Categories Spending More Than ₹800:\n")

    for category in high_expenses:
        file.write(category + "\n")

    file.close()

    print("Report Generated Successfully in report.txt")


# Main Menu
while True:

    print("\n===== Expense Tracker Menu =====")
    print("1. Display All Expenses")
    print("2. Calculate Total Expenditure")
    print("3. Highest & Lowest Expense")
    print("4. Display Expenses Above ₹800")
    print("5. Add New Expense Category")
    print("6. Update Expense Amount")
    print("7. Generate Report")
    print("8. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        display_expenses()

    elif choice == "2":
        total_expenditure()

    elif choice == "3":
        highest_lowest_expense()

    elif choice == "4":
        expenses_above_800()

    elif choice == "5":
        add_expense()

    elif choice == "6":
        update_expense()

    elif choice == "7":
        generate_report()

    elif choice == "8":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")