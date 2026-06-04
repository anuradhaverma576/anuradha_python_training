secret_number = 7

while True:
    guess = int(input("Guess the Number: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong Guess. Try Again.")