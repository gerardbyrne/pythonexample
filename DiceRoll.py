import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")

    dice1Value = random.randint(min, max)
    dice2Value = random.randint(min, max)
    print (dice1Value)
    print (dice2Value)

    if (dice1Value + dice2Value == 6):
        print("Well done - you have a six")
    elif (dice1Value + dice2Value != 6):
        print("Better luck next roll")

    roll_again = input("Roll the dices again?")