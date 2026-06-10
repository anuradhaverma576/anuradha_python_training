# Library Book Issue System


# Function to read book data from file
def read_books():

    books = []

    file = open("books.txt", "r")

    for line in file:

        data = line.strip().split(",")

        book = {
            "id": data[0],
            "name": data[1],
            "quantity": int(data[2])
        }

        books.append(book)

    file.close()

    return books


# Function to update file
def update_file(books):

    file = open("books.txt", "w")

    for book in books:

        line = (
            book["id"] + "," +
            book["name"] + "," +
            str(book["quantity"]) + "\n"
        )

        file.write(line)

    file.close()


# Function to display all books
def display_books():

    books = read_books()

    print("\nBook Records")
    print("-" * 40)

    for book in books:
        print(book["id"],
              book["name"],
              "Quantity:", book["quantity"])


# Function to search a book
def search_book():

    book_id = input("Enter Book ID: ")

    books = read_books()

    found = False

    for book in books:

        if book["id"] == book_id:

            print("\nBook Found")
            print("Book ID:", book["id"])
            print("Book Name:", book["name"])
            print("Quantity:", book["quantity"])

            found = True
            break

    if found == False:
        print("Book Not Found")


# Function to issue a book
def issue_book():

    book_id = input("Enter Book ID to Issue: ")

    books = read_books()

    found = False

    for book in books:

        if book["id"] == book_id:

            found = True

            if book["quantity"] > 0:
                book["quantity"] -= 1

                update_file(books)

                print("Book Issued Successfully")

            else:
                print("Book Not Available")

            break

    if found == False:
        print("Book ID Not Found")


# Function to return a book
def return_book():

    book_id = input("Enter Book ID to Return: ")

    books = read_books()

    found = False

    for book in books:

        if book["id"] == book_id:

            book["quantity"] += 1

            update_file(books)

            print("Book Returned Successfully")

            found = True
            break

    if found == False:
        print("Book ID Not Found")


# Function to display unavailable books
def unavailable_books():

    books = read_books()

    print("\nUnavailable Books")
    print("-" * 30)

    for book in books:

        if book["quantity"] == 0:
            print(book["name"])


# Function to display books requiring restocking
def restocking_books():

    books = read_books()

    print("\nBooks Requiring Restocking")
    print("-" * 35)

    for book in books:

        if book["quantity"] < 2:
            print(book["name"],
                  "- Copies:",
                  book["quantity"])


# Main Menu
while True:

    print("\n===== Library Menu =====")
    print("1. Display All Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Display Restocking Books")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        display_books()

    elif choice == "2":
        search_book()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        unavailable_books()

    elif choice == "6":
        restocking_books()

    elif choice == "7":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")