books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# Unavailable books
print("Unavailable Books:")

for book in books:
    if books[book] == 0:
        print(book)

# Count available books
count = 0

for book in books:
    if books[book] > 0:
        count += 1

print("\nAvailable Books:", count)

# Book with maximum copies
maximum = max(books, key=books.get)

print("\nBook with Maximum Copies:")
print(maximum, books[maximum])

# Books with less than 3 copies
low_books = []

for book in books:
    if books[book] < 3:
        low_books.append(book)

print("\nBooks with less than 3 copies:")
print(low_books)

# Total books available
total = 0

for book in books:
    total += books[book]

print("\nTotal Number of Books:", total)