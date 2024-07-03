import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


human_sign = " "
comp_sign = " "
result = ["Draw", "You Win", "Comp Wins"]


choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n: "))

if choice == 0:
    human_sign = rock
elif choice == 1:
    human_sign = paper
elif choice == 2:
    human_sign = scissors
else:
    print("Invalid input")


comp_choice = random.randint(0, 2)

if comp_choice == 0:
    comp_sign = rock
elif comp_choice == 1:
    comp_sign = paper
elif comp_choice == 2:
    comp_sign = scissors
else:
    print("Invalid input")

print("You:\n" + human_sign)
print("Comp:\n" + comp_sign)


def result_calculation():
    result_index = (choice - comp_choice + 3) % 3
    return result[result_index]

print (result_calculation())