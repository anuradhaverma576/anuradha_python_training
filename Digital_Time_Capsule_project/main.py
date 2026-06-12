from authentication import register_user, login_user

from capsule_management import (
    create_capsule,
    view_capsules,
    update_capsule,
    delete_capsule,
    search_capsule,
    generate_report
)


def capsule_menu():

    while True:

        print("\n===== DIGITAL TIME CAPSULE =====")
        print("1. Create Capsule")
        print("2. View Capsules")
        print("3. Update Capsule")
        print("4. Delete Capsule")
        print("5. Search Capsule")
        print("6. Generate Report")
        print("7. Logout")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            create_capsule()

        elif choice == 2:
            view_capsules()

        elif choice == 3:
            update_capsule()

        elif choice == 4:
            delete_capsule()

        elif choice == 5:
            search_capsule()

        elif choice == 6:
            generate_report()

        elif choice == 7:
            print("Logout Successful")
            break

        else:
            print("Invalid Choice")


def main_menu():

    while True:

        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            register_user()

        elif choice == 2:

            success = login_user()

            if success:
                capsule_menu()

        elif choice == 3:
            print("Thank You")
            break

        else:
            print("Invalid Choice")


main_menu()