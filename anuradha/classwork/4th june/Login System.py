correct_password = "admin123"
password = ""

while password != correct_password:
    password = input("Enter Password: ")

    if password != correct_password:
        print("Incorrect Password. Try Again.")

print("Login Successful.")