import random
import art
from game_data import people
from replit import clear
import time




def play_game():
    print(art.logo)
    score = 0
    game_continue = True

    first_person = random.choice(list(people.items()))
    second_person = random.choice(list(people.items()))

    while game_continue:
        while first_person == second_person:
            second_person = random.choice(list(people.items()))

        clear()
        print(f"Score: {score}")
        time.sleep(2)
        print(f"\nCompare A: {first_person[0]}")
        print(art.vs)
        print(f"Compare B: {second_person[0]}")

        answer = input("Who do you think has more followers (A / B): ").upper()

        first_person_followers = first_person[1]
        second_person_followers = second_person[1]

        if (first_person_followers > second_person_followers and answer == 'A') or (
                second_person_followers > first_person_followers and answer == 'B'):
            score += 1
            print("Correct!")
            time.sleep(2)
            first_person = second_person
            second_person = random.choice(list(people.items()))
        else:
            game_continue = False
            print("Incorrect! Your score was:", score)
            time.sleep(2)


while True:
    play_game()
    play_again = input("Play again? (yes / no): ").lower()

    if play_again == 'no':
        break
