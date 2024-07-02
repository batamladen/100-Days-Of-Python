print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill?: "))
tip_percentage = int(input("What percentage tip would you like to give?: "))
amount_of_people = int(input("How many people to split the bill?: "))

result = (total_bill + (total_bill * tip_percentage/100)) / amount_of_people

print(result)