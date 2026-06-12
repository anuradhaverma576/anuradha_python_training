def register_user():

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    file = open("users.txt", "a")

    file.write(username + "," + password + "\n")

    file.close()

    print("Registration Successful!")


def login_user():

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    file = open("users.txt", "r")

    users = file.readlines()

    file.close()

    for user in users:

        data = user.strip().split(",")

        if username == data[0] and password == data[1]:

            print("Login Successful!")
            return True

    print("Invalid Username or Password")
    return False