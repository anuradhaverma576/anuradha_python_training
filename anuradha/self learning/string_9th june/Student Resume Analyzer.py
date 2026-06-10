# Student Resume Analyzer

# Sample Resume Text
resume = """
Name: Rahul Sharma

Skills: Python, SQL, Java, React, Python, Communication,
Teamwork, SQL, Problem Solving, React

Education:
B.Tech in Computer Science

Projects:
Student Management System
Online Shopping Website

Achievements:
Won Coding Competition

Email: rahul123@gmail.com
Phone: 9876543210
"""

# Convert resume text to lowercase words
words = resume.lower().split()

# Count total words
total_words = len(words)

# Count total characters
total_characters = len(resume)

# Extract Email IDs
emails = []

for word in resume.split():
    if "@" in word and "." in word:
        emails.append(word)

# Extract Phone Numbers
phone_numbers = []

for word in resume.split():
    clean_word = word.strip()

    if clean_word.isdigit() and len(clean_word) == 10:
        phone_numbers.append(clean_word)

# Skill List
skills = [
    "python", "sql", "java", "react",
    "communication", "teamwork",
    "problem", "solving"
]

# Count skills mentioned
skill_count = {}

for skill in skills:
    count = resume.lower().count(skill)

    if count > 0:
        skill_count[skill] = count

# Find repeated keywords
print("Repeated Keywords")
print("-" * 30)

for word in words:
    clean_word = word.strip(",.:")

    if words.count(clean_word) > 1:
        print(clean_word)

# Find most frequently used word
frequency = {}

for word in words:
    clean_word = word.strip(",.:")

    if clean_word in frequency:
        frequency[clean_word] += 1
    else:
        frequency[clean_word] = 1

most_frequent_word = ""
highest_count = 0

for word in frequency:
    if frequency[word] > highest_count:
        highest_count = frequency[word]
        most_frequent_word = word

# Skill Frequency Report
print("\nSkill Frequency Report")
print("-" * 30)

for skill in skill_count:
    print(skill, "->", skill_count[skill])

# Detect duplicate skills
print("\nDuplicate Skills")
print("-" * 30)

for skill in skill_count:
    if skill_count[skill] > 1:
        print(skill)

# Top 5 Keywords
sorted_keywords = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nResume Analysis Report")
print("-" * 35)

print("Total Words:", total_words)
print("Total Characters:", total_characters)

print("\nEmail Found:", len(emails))
for email in emails:
    print(email)

print("\nPhone Numbers Found:", len(phone_numbers))
for number in phone_numbers:
    print(number)

print("\nMost Frequent Word:", most_frequent_word)

print("\nTop 5 Keywords")
for i in range(min(5, len(sorted_keywords))):
    print(sorted_keywords[i][0])