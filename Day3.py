print("Welcome to the tresure island!")
print("Your mission is to find the tessure.\n")

print("You are walking ang getting near a crossroad, do you go on it or continue ahead?")
choice_1 = input("(go on it / continue): ")

if choice_1 == "go on it":
    print("\nYou didn't look and a car hit you.")
    exit()

else:
    print("\nYou see a smoke on the left and a huge tree on the right. Where do u go?")
    choice_2 = input("(smoke / tree): ")

    if choice_2 == "smoke":
        print("\nYou went in the middle of a gang war and got a bullet in your head.")
        exit()

    elif choice_2 == "tree":
        print("\nAn elf came to you saying he will help you find the treasure. Do you accept the help?")
        choice_3 = input("(yes / no): ")

        if choice_3 == "yes":
            print("\nHe took you to the 'X' spot and asks to take the showel and dig the treaure, do you give him the showel?")
            choice_4 = input("(yes / no): ")

            if choice_4 == "yes":
                print("\nHe used the showel and hit you in the head.")
                exit()

            elif choice_4 == "no":
                print("\nYou reject and kill him with the showel now that you know where the 'X' is.")

                print("You're thinking if its better to dig up the elf first or the 'X' spot.")
                choice_6 = input("(elf first/ X spot first): ")

                if choice_6 == "elf first":
                    print("\nWhile digging a hole for the elf, a group of elfs pushes you in it and digs you up.")
                    exit()

                elif choice_6 == "X spot first":
                    print("\nYou found the reasure and went home with it!!!")


        elif choice_3 == "no":
            print("\nYou walk to the tree alone and after some time find a 'X' spot. Do you dig it?")
            choice_5 = input("(yes / no ): ")

            if choice_5 == "yes":
                print("\nYou found the treasure!!!")

            elif choice_5 == "no":
                print("\nYou continue to search and a group of elfs kills you.")
                exit()

