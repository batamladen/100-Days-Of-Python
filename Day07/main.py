import random
import art
from wordlist import WORDLIST
import os

lives = 6
used_letters = []
word = []

chosen_word = random.choice(WORDLIST)
word.extend(chosen_word)

welcome_message = art.logo3
win_message = art.logo2
start_photo = art.stages[lives]

print(welcome_message)
print("To win, guess the word!")
print(start_photo)

# Initialize displayed_word with underscores
displayed_word = ['_' for _ in chosen_word]

while lives != 0:
    print("\nused_letters: ", used_letters)
    print(' '.join(displayed_word))
    guess_letter = input("Guess a letter: ").lower()

    if not guess_letter.isalpha() or len(guess_letter) != 1:
        print("Input only a single letter.")
        continue

    if guess_letter not in used_letters:
        used_letters.append(guess_letter)
    else:
        print("Letter already used")
        continue

    if guess_letter in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess_letter:
                displayed_word[index] = guess_letter
    else:
        lives -= 1
        start_photo = art.stages[lives]

    print(start_photo)

    if '_' not in displayed_word:
        print("Congratulations! You've guessed the word!")
        print(win_message)
        break

if lives == 0:
    print("You've run out of lives. The word was:", ''.join(chosen_word))
