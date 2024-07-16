from art import logo
import random

def play_game():
    difficulty_easy = 10
    difficulty_hard = 5

    number_picker = random.randint(1, 100)

    print("\nWelcome to \n" + logo)
    print("I'm thinking of a number between 1 and 100, try to guess it!")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        lives = difficulty_easy
        while lives != 0:
            print("\nYou have", lives, "guesses left")
            guess = int(input("Take a guess: "))

            if guess == number_picker:
                print("Correct! The number was ", number_picker)
                break
            elif guess < number_picker:
                print("Higher")
                lives -= 1
            elif guess > number_picker:
                print("Lower")
                lives -= 1

    elif difficulty == 'hard':
        lives = difficulty_hard
        while lives != 0:
            print("\nYou have", lives, "guesses left")
            guess = int(input("Take a guess: "))

            if guess == number_picker:
                print("Correct! The number was ", number_picker)
                break
            elif guess < number_picker:
                print("Higher")
                lives -= 1
            elif guess > number_picker:
                print("Lower")
                lives -= 1

    if lives == 0:
        print(f"\nSorry, you've run out of guesses. The number was {number_picker}.")

while True:
    play_game()
    play_again = input("Do you want to play again? ('yes' / 'no'): ").lower()
    if play_again != 'yes':
        print("Goodbye.")
        break
