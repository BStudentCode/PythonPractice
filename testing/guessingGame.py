secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("Congratulations!")
        break  # terminates while loop, stops asking for guesses if user gets the right number
    else:
        print("Wrong guess!")

else:
    print("You have used up your guesses.")