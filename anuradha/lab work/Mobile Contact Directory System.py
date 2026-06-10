# Mobile Contact Directory System


# Function to read contacts from file
def read_contacts():

    contacts = []

    file = open("contacts.txt", "r")

    for line in file:

        data = line.strip().split(",")

        contact = {
            "name": data[0],
            "number": data[1]
        }

        contacts.append(contact)

    file.close()

    return contacts


# Function to update file
def update_file(contacts):

    file = open("contacts.txt", "w")

    for contact in contacts:

        line = (
            contact["name"] + "," +
            contact["number"] + "\n"
        )

        file.write(line)

    file.close()


# Function to display all contacts
def display_contacts():

    contacts = read_contacts()

    print("\nContact List")
    print("-" * 30)

    for contact in contacts:
        print(contact["name"],
              "-",
              contact["number"])


# Function to search contact by name
def search_contact():

    name = input("Enter Contact Name: ")

    contacts = read_contacts()

    found = False

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            print("\nContact Found")
            print("Name:", contact["name"])
            print("Number:", contact["number"])

            found = True
            break

    if found == False:
        print("Contact Not Found")


# Function to add new contact
def add_contact():

    name = input("Enter Name: ")
    number = input("Enter Number: ")

    file = open("contacts.txt", "a")

    file.write("\n" + name + "," + number)

    file.close()

    print("Contact Added Successfully")


# Function to update contact number
def update_contact():

    name = input("Enter Contact Name: ")

    contacts = read_contacts()

    found = False

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            new_number = input("Enter New Number: ")

            contact["number"] = new_number

            update_file(contacts)

            print("Contact Updated Successfully")

            found = True
            break

    if found == False:
        print("Contact Not Found")


# Function to delete contact
def delete_contact():

    name = input("Enter Contact Name to Delete: ")

    contacts = read_contacts()

    new_contacts = []
    found = False

    for contact in contacts:

        if contact["name"].lower() == name.lower():
            found = True

        else:
            new_contacts.append(contact)

    if found:

        update_file(new_contacts)

        print("Contact Deleted Successfully")

    else:
        print("Contact Not Found")


# Function to display contacts starting with vowel
def vowel_contacts():

    contacts = read_contacts()

    print("\nContacts Starting With Vowel")
    print("-" * 35)

    vowels = "AEIOUaeiou"

    for contact in contacts:

        if contact["name"][0] in vowels:
            print(contact["name"],
                  "-",
                  contact["number"])


# Main Menu
while True:

    print("\n===== Contact Directory Menu =====")
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add New Contact")
    print("4. Update Contact Number")
    print("5. Delete Contact")
    print("6. Display Vowel Contacts")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        display_contacts()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        add_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        vowel_contacts()

    elif choice == "7":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")