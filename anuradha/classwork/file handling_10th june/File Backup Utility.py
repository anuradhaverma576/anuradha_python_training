# File Backup Utility


# Function to copy file content
def backup_file():

    # Input source and destination file names
    source_file = input("Enter Source File Name: ")
    destination_file = input("Enter Destination File Name: ")

    try:
        # Open source file in read mode
        file1 = open(source_file, "r")

        # Read all content
        content = file1.read()

        file1.close()

        # Open destination file in write mode
        file2 = open(destination_file, "w")

        # Write content into destination file
        file2.write(content)

        file2.close()

        # Success message
        print("\nFile copied successfully.")
        print("All contents from",
              source_file,
              "have been copied to",
              destination_file)

    except FileNotFoundError:
        print("Source file not found.")


# Function Calling
backup_file()