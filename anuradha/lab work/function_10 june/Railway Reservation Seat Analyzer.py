# Railway Reservation Seat Analyzer

# List of seats
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# Function to count booked and available seats
def count_seats(seats):
    booked = 0
    available = 0

    for seat in seats:
        if seat == "Booked":
            booked += 1
        elif seat == "Available":
            available += 1

    return booked, available


# Function to find first available seat
def first_available(seats):

    for i in range(len(seats)):
        if seats[i] == "Available":
            return i + 1   # Seat number starts from 1

    return "No seat available"


# Function to calculate occupancy percentage
def occupancy_percentage(seats):

    booked = 0

    for seat in seats:
        if seat == "Booked":
            booked += 1

    percentage = (booked / len(seats)) * 100
    return percentage


# Function to display available seat numbers
def display_available_seats(seats):

    print("Available Seat Numbers:")

    for i in range(len(seats)):
        if seats[i] == "Available":
            print(i + 1, end=" ")


# Function Calling
booked, available = count_seats(seats)

print("Booked Seats:", booked)
print("Available Seats:", available)

print("\nFirst Available Seat:", first_available(seats))

print("\nOccupancy Percentage:",
      round(occupancy_percentage(seats), 2), "%")

display_available_seats(seats)