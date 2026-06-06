correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

score = 0
wrong_questions = []

# Calculate score
for i in range(len(correct)):
    if correct[i] == student[i]:
        score += 1
    else:
        wrong_questions.append(i + 1)

print("Score:", score)

# Incorrect questions
print("\nIncorrect Question Numbers:")
print(wrong_questions)

# Correct and wrong answers
correct_count = score
wrong_count = len(correct) - score

print("\nCorrect Answers:", correct_count)
print("Wrong Answers:", wrong_count)

# Pass/Fail
percentage = (score / len(correct)) * 100

if percentage >= 60:
    print("\nResult: Pass")
else:
    print("\nResult: Fail")