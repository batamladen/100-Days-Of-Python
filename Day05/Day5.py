import random

print("Welcome to the Password Generator!")

letters_number = int(input("What length do you want your password to be?: "))
symbols_number = int(input("How many symbols would you like in your password?: "))
numbers_number = int(input("How many numbers would you like in your password?: "))

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
           'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

symbols = ['!', '@', '#', '%', '^', '&', '*', '(', ')',
           '_', '-', '/', '*', '+', '~', '`']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

#add upercase
def password_strength():

    if letters_number <= 5:
        print("Password Strength: Weak")

    if letters_number > 5  and symbols_number < 1 and numbers_number > 0:
        print("Password Strength: Medium")

    if letters_number >= 7 and symbols_number > 0 and numbers_number >= 2:
        print("Password Strength: Strong")


slice_end = (symbols_number + numbers_number)

password = []

for i in range(letters_number):
    password.append(random.choice(letters))

for j in range(symbols_number):
    password.append(random.choice(symbols))

for k in range(numbers_number):
    password.append(random.choice(numbers))

del password[0:slice_end]
random.shuffle(password)

final_password = ''.join(password)
print("\nFinal Password: " + final_password)


if symbols_number > letters_number:
    print("Error: Amount of desired symbols greather than password length")
if numbers_number > letters_number:
    print("Error: Amount of desired numbers greather than password length")
if numbers_number > (letters_number - symbols_number):
    print("Error: Desired password length: ", letters_number, ", amount of desired symbols and numbers:", (symbols_number + numbers_number))
#add "very strong" if user wants uppercase leeters with the symbols and numbers

password_strength()


