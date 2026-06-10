# Student Result Processing System


# Function to read student data from file
def read_students():

    students = []

    file = open("results.txt", "r")

    for line in file:

        data = line.strip().split(",")

        student = {
            "id": data[0],
            "name": data[1],
            "marks": int(data[2])
        }

        students.append(student)

    file.close()

    return students


# Function to update grades file
def write_grades(students):

    file = open("grades.txt", "w")

    for student in students:

        marks = student["marks"]

        # Grade Calculation
        if marks >= 90:
            grade = "A"

        elif marks >= 75:
            grade = "B"

        elif marks >= 40:
            grade = "C"

        else:
            grade = "F"

        # Write into grades file
        line = (
            student["id"] + "," +
            student["name"] + "," +
            str(marks) + "," +
            grade + "\n"
        )

        file.write(line)

    file.close()


# Function to display all student records
def display_students():

    students = read_students()

    print("\nStudent Records")
    print("-" * 40)

    for student in students:

        print(student["id"],
              student["name"],
              student["marks"])


# Function to search student by ID
def search_student():

    student_id = input("Enter Student ID: ")

    students = read_students()

    found = False

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Found")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])

            found = True
            break

    if found == False:
        print("Student Not Found")


# Function to find topper and lowest scorer
def topper_lowest():

    students = read_students()

    topper = students[0]
    lowest = students[0]

    for student in students:

        if student["marks"] > topper["marks"]:
            topper = student

        if student["marks"] < lowest["marks"]:
            lowest = student

    print("\nTopper")
    print(topper["name"],
          "-",
          topper["marks"])

    print("\nLowest Scorer")
    print(lowest["name"],
          "-",
          lowest["marks"])


# Function to calculate class average
def class_average():

    students = read_students()

    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)

    print("Class Average =", average)


# Function to count pass and fail students
def pass_fail_count():

    students = read_students()

    passed = 0
    failed = 0

    for student in students:

        if student["marks"] >= 40:
            passed += 1
        else:
            failed += 1

    print("Passed Students:", passed)
    print("Failed Students:", failed)


# Function to generate grades
def generate_grades():

    students = read_students()

    print("\nStudent Grades")
    print("-" * 30)

    for student in students:

        marks = student["marks"]

        if marks >= 90:
            grade = "A"

        elif marks >= 75:
            grade = "B"

        elif marks >= 40:
            grade = "C"

        else:
            grade = "F"

        print(student["name"],
              "->",
              grade)

    # Save grades to file
    write_grades(students)

    print("\nGrades written to grades.txt")


# Main Menu
while True:

    print("\n===== Student Result Menu =====")
    print("1. Display All Students")
    print("2. Search Student by ID")
    print("3. Find Topper & Lowest Scorer")
    print("4. Calculate Class Average")
    print("5. Count Pass & Fail Students")
    print("6. Generate Grades")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        display_students()

    elif choice == "2":
        search_student()

    elif choice == "3":
        topper_lowest()

    elif choice == "4":
        class_average()

    elif choice == "5":
        pass_fail_count()

    elif choice == "6":
        generate_grades()

    elif choice == "7":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")