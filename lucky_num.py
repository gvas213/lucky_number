import random

#intro
name = input("Please enter your name: ")
play = input(f"Would you like to play the lucky number game? Enter 'y' for yes or 'n' for no: ")

while play.lower() != 'n' and play.lower() != 'y':
    play = input(f"Sorry that wasn't an option. Please enter 'y' for yes or 'n' for no: ")

#playing decision
while play.lower() == 'y':

    comp_numbers = []
    user_list = []
    comp_list = []
    match_list = []

# create user list of 5
    while len(user_list) <=4:
        user_num = int(input("enter a number 1-70: "))

        while str(user_num).isnumeric() == False or int(user_num) < 1 or int(user_num) > 70:
            user_num = input("Sorry that's not an option. Please enter a number 1-70: ")

        user_list.append(user_num)

#create computer list of 5
    for x in range (1, 6):
        comp_num = random.randint(1, 70)
        comp_list.append(comp_num)

#check for matches
    for i in comp_list:
            if i in user_list:
                match_list.append(i)

#game results:
    correct = (len(match_list))
    
    if len(match_list) > 0:
        print(f"here are your matches: {match_list}")

    user_list.sort()
    comp_list.sort()

    user_list =  str(user_list)
    comp_list = str(comp_list)

    if correct == 1:
        points = "1"
    elif correct == 2:
        points = "4"
    elif correct == 3:
        points = "10"
    elif correct == 4:
        points = "30"
    elif correct == 5:
        points = "100"
    else:
        points = "0"

    
    #points and play again prompt
    print(f"the numbers you chose were {user_list}")
    print(f"the numbers the computer chose were {comp_list}")
    print(f"you guessed {correct} correct and earned {points}")
    play = input(f"Would you like to play again? Please enter 'y' for yes or 'n' for no: ")


    while play.lower() != 'n' and play.lower() != 'y':
        play = input(f"Sorry that wasn't an option. Please enter 'y' for yes or 'n' for no: ")

print("thanks for playing")


# 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