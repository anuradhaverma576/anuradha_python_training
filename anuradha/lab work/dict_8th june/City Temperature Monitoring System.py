# Dictionary storing city temperatures
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# Display cities above 40 degree Celsius
print("Cities Above 40°C:")

for city in temperature:
    if temperature[city] > 40:
        print(city)

# Find hottest city
hottest_city = ""
highest_temp = 0

for city in temperature:
    if temperature[city] > highest_temp:
        highest_temp = temperature[city]
        hottest_city = city

print("\nHottest City:", hottest_city, "(", highest_temp, "°C)", sep="")

# Find coolest city
coolest_city = ""
lowest_temp = 99999

for city in temperature:
    if temperature[city] < lowest_temp:
        lowest_temp = temperature[city]
        coolest_city = city

print("Coolest City:", coolest_city, "(", lowest_temp, "°C)", sep="")

# Calculate average temperature
total_temp = 0

for city in temperature:
    total_temp += temperature[city]

average = total_temp / len(temperature)

print("Average Temperature:", average)

# Create list of pleasant cities
pleasant = []

for city in temperature:
    if temperature[city] < 35:
        pleasant.append(city)

print("Pleasant Cities:")
print(pleasant)

# Count cities between 35°C and 40°C
count = 0

for city in temperature:
    if temperature[city] >= 35 and temperature[city] <= 40:
        count += 1

print("Cities Between 35°C and 40°C:", count)