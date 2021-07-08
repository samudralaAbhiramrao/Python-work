import random

min_value = 1
max_value = 6


roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the Dice")
    print("The values are :")

    # Generating the random Dice values using the randint()

    print(f"Dice1 Value : {random.randint(min_value, max_value)}")

    print(f"Dice2 Value: {random.randint(min_value, max_value)}")

    roll_again = input("Do you want to Roll the Dice Again ??")
