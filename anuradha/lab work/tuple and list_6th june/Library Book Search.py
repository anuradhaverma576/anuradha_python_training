books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# Display unavailable books
print("Unavailable Books:")

for book in books:
    if book[1] == 0:
        print(book[0])

# Books with more than 2 copies
print("\nBooks with more than 2 copies:")

for book in books:
    if book[1] > 2:
        print(book[0])

# Count available books
count = 0

for book in books:
    if book[1] > 0:
        count += 1

print("\nAvailable Books:", count)

# Search for requested book
search = input("\nEnter book name to search: ")

for book in books:
    if book[0] == search:
        print("Book Found")
        break