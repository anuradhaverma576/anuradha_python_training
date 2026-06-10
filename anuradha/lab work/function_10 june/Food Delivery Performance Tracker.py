# Food Delivery Performance Tracker

# List of delivery times
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]


# Function to find fastest delivery
def fastest_delivery(times):

    shortest = times[0]

    for time in times:
        if time < shortest:
            shortest = time

    return shortest


# Function to return delayed orders
def delayed_orders(times):

    delayed = []

    for time in times:
        if time > 45:
            delayed.append(time)

    return delayed


# Function to calculate average delivery time
def average_delivery_time(times):

    total = 0

    for time in times:
        total += time

    average = total / len(times)

    return average


# Function to display delivery categories
def delivery_category(times):

    print("Categories:")

    for time in times:

        if time <= 30:
            print(time, "-> Fast")

        elif time <= 45:
            print(time, "-> Normal")

        else:
            print(time, "-> Delayed")


# Function Calling
print("Fastest Delivery:",
      fastest_delivery(delivery_time), "minutes")

print("\nDelayed Orders:")
print(delayed_orders(delivery_time))

print("\nAverage Delivery Time:")
print(round(average_delivery_time(delivery_time), 1),
      "minutes")

delivery_category(delivery_time)