contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# Contact names in alphabetical order
print("Contacts in alphabetical order:")

for name in sorted(contacts):
    print(name)

# Total contacts
print("\nTotal Contacts:", len(contacts))

# Search contact
search = input("\nEnter contact name: ")
found = False

for name in contacts:
    if name == search:
        print("Contact Found:", contacts[name])
        found = True
        break

if found == False:
    print("Contact Not Found")

# Names starting with vowels
vowel_contacts = []

for name in contacts:
    if name[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        vowel_contacts.append(name)

print("\nNames starting with vowels:")
print(vowel_contacts)