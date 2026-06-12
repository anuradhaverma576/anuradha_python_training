def create_capsule():

    capsule_id = input("Enter Capsule ID: ")
    title = input("Enter Title: ")
    message = input("Enter Message: ")
    creation_date = input("Enter Creation Date: ")
    unlock_date = input("Enter Unlock Date: ")

    status = "Locked"

    file = open("capsules.txt", "a")

    file.write(
        capsule_id + "|" +
        title + "|" +
        message + "|" +
        creation_date + "|" +
        unlock_date + "|" +
        status + "\n"
    )

    file.close()

    print("Capsule Created Successfully!")


def view_capsules():

    file = open("capsules.txt", "r")

    data = file.readlines()

    file.close()

    print("\nAll Capsules:")

    for line in data:

        capsule = line.strip().split("|")

        print("ID:", capsule[0])
        print("Title:", capsule[1])
        print("Message:", capsule[2])
        print("Unlock Date:", capsule[4])
        print("-------------------")


def update_capsule():

    capsule_id = input("Enter Capsule ID to Update: ")

    file = open("capsules.txt", "r")

    data = file.readlines()

    file.close()

    updated_data = []

    found = False

    for line in data:

        capsule = line.strip().split("|")

        if capsule[0] == capsule_id:

            found = True

            new_title = input("Enter New Title: ")
            new_message = input("Enter New Message: ")

            capsule[1] = new_title
            capsule[2] = new_message

        updated_line = "|".join(capsule)
        updated_data.append(updated_line + "\n")

    file = open("capsules.txt", "w")
    file.writelines(updated_data)
    file.close()

    if found:
        print("Capsule Updated Successfully!")
    else:
        print("Capsule ID Not Found")


def delete_capsule():

    capsule_id = input("Enter Capsule ID to Delete: ")

    file = open("capsules.txt", "r")

    data = file.readlines()

    file.close()

    new_data = []

    found = False

    for line in data:

        capsule = line.strip().split("|")

        if capsule[0] == capsule_id:

            found = True
            print("Capsule Deleted Successfully!")
            continue

        new_data.append(line)

    file = open("capsules.txt", "w")
    file.writelines(new_data)
    file.close()

    if found == False:
        print("Capsule ID Not Found")


def search_capsule():

    title = input("Enter Title to Search: ")

    file = open("capsules.txt", "r")

    data = file.readlines()

    file.close()

    found = False

    for line in data:

        capsule = line.strip().split("|")

        if title.lower() in capsule[1].lower():

            found = True

            print("ID:", capsule[0])
            print("Title:", capsule[1])
            print("Message:", capsule[2])

    if found == False:
        print("No Capsule Found")


def generate_report():

    file = open("capsules.txt", "r")

    data = file.readlines()

    file.close()

    total_capsules = len(data)

    locked = 0
    unlocked = 0

    titles = set()

    for line in data:

        capsule = line.strip().split("|")

        titles.add(capsule[1])

        if capsule[5] == "Locked":
            locked += 1
        else:
            unlocked += 1

    report = (
        total_capsules,
        locked,
        unlocked
    )

    print("\n===== REPORT =====")
    print("Total Capsules:", report[0])
    print("Locked Capsules:", report[1])
    print("Unlocked Capsules:", report[2])
    print("Unique Titles:", len(titles))

    