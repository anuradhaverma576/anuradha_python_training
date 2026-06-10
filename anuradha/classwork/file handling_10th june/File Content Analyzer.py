# File Content Analyzer


# Function to analyze file content
def analyze_file():

    # Open file in read mode
    file = open("article.txt", "r")

    # Read complete file content
    content = file.read()

    # Move cursor to beginning
    file.seek(0)

    # Read all lines
    lines = file.readlines()

    # Close file
    file.close()

    # Count vowels
    vowels = 0

    for ch in content.lower():

        if ch in "aeiou":
            vowels += 1

    # Count total characters
    total_characters = len(content)

    # Count total lines
    total_lines = len(lines)

    # Display Report
    print("File Analysis Report")
    print("-" * 30)

    print("Total Number of Vowels    :", vowels)
    print("Total Number of Characters:", total_characters)
    print("Total Number of Lines     :", total_lines)


# Function Calling
analyze_file()