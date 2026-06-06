bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# 1. Display confirmed passengers
print("Confirmed Passengers:")

for booking in bookings:
    if booking[2] == "Confirmed":
        print(booking[0], booking[1])

# 2. Count passengers travelling to Delhi
delhi_count = 0

for booking in bookings:
    if booking[1] == "Delhi":
        delhi_count += 1

print("\nPassengers Travelling to Delhi:", delhi_count)

# 3. Count booking status
confirmed = 0
waiting = 0
cancelled = 0

for booking in bookings:
    if booking[2] == "Confirmed":
        confirmed += 1
    elif booking[2] == "Waiting":
        waiting += 1
    elif booking[2] == "Cancelled":
        cancelled += 1

print("\nConfirmed:", confirmed)
print("Waiting:", waiting)
print("Cancelled:", cancelled)

# 4. List of waiting passengers
waiting_list = []

for booking in bookings:
    if booking[2] == "Waiting":
        waiting_list.append(booking[0])

print("\nWaiting List:")
print(waiting_list)

# 5. Most booked destination
destinations = {}

for booking in bookings:
    city = booking[1]

    if city in destinations:
        destinations[city] += 1
    else:
        destinations[city] = 1

most_booked = max(destinations, key=destinations.get)

print("\nMost Booked Destination:")
print(most_booked)