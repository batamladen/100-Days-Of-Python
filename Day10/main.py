
def multiplication(a, b):
    multiplication_result = a * b
    return multiplication_result

def devision(a, b):
    devision_result = a / b
    return devision_result

def sum(a, b):
    sum_result = a + b
    return sum_result

def subtraction(a, b):
    subtraction_result = a - b
    return subtraction_result

run = True

first_number = int(input("1st number: "))

while run:
    first_operation = input("Choose operation (+, -, *, /): ")
    second_number = int(input("2nd number: "))

    operations = {
        '+' : sum,
        '-' : subtraction,
        '*' : multiplication,
        '/' : devision
    }

    calculation = operations[first_operation]
    answer = calculation(first_number, second_number)
    print(f"{first_number} {first_operation} {second_number} = {answer}")

    next = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to exit: ")

    if next == 'y':
        run = True
        first_number = answer
    elif next == 'n':
        run = False
    else:
        print("Invalid input")
        run = False
        print("\nGoodbye")
