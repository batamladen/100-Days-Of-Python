from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']



def cesar(start_text, shift_amount, chiper_direction):
    end_text = ""

    if chiper_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char.isalpha():
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

        else:
            end_text += char

    print(f"Here's the {chiper_direction} result: {end_text}\n")


run = True

while run:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % shift == 0

    cesar(text, shift, direction)

    choice = input("Do you want to run this program again?\nType 'yes' or 'no': ")
    if choice == "no":
        run = False
        print("Goodbye")