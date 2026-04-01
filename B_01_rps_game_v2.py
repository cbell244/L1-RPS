import random

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # get user response ad make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        #print error if user inputs something wrong
        print(error)
        print()


#Displays instructions
def instructions():
    """prints instructions"""

    print("""
    *** Instructions ***

    To begin, choose the number of rounds (or press <enter> to play infinite mode).

    Then, play against the computer. You need to choose to play R (rock), P (paper), or S (scissors).

    The rules are as follows:
    o Paper beats rock
    o Rock beats scissors
    o Scissors beats paper

    During the game, if you'd like to stop playing, enter 'xxx'.

    Good luck!
        """)


#checks for an integer of more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        #check for infinite mode
        if to_check == "":
            return "infinite"


        try:
            response = int(to_check)

            # checks that the number is more than 0
            if response < 1:
                 print(error)

            else:
                return response

        except ValueError:
            print(error)


# compares user and comp choices
def rps_compare(user, comp):

        # if the user and the computer choice is the same, it's a tie
        if user == comp:
            round_result = "tie"

        # there are three ways to win
        elif user == "paper" and comp == "rock":
            round_result = "win"
        elif user == "scissors" and comp == "paper":
            round_result = "win"
        elif user == "rock" and comp == "scissors":
            round_result = "win"

        # if it's not a win/ tie then it's a loss :/
        else:
            round_result = "lose"

        return round_result


# main routine starts here

# initialise game variables
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

print("🪨📃✂️ Rock / Paper / Scissors Game ✂️📃🪨")
print()

# asl user if they want to see te instructions and display them if requested
want_instructions = string_checker("Do you want the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like to play? Press <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5


# game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n🏁🏁🏁 Round {rounds_played + 1} (Infinite mode) 🏁🏁🏁"

    if mode == "regular":
        rounds_heading = f"\n🏁🏁🏁 Round {rounds_played + 1} of {num_rounds} 🏁🏁🏁"

    print(rounds_heading)
    print()


    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("Computer chose", comp_choice)

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("You chose", user_choice)

    #check if user inputs exit code
    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)

    #Adjust game lost / game ties counters and add results to game history
    if result == 'lose':
        rounds_lost += 1
        feedback = "😭😭😭 You lost!!! 😭😭😭"
    elif result == 'tie':
        rounds_tied += 1
        feedback = "😒😒😒 You tied... 😒😒😒"
    else:
        feedback = "😎😎😎 You won!!! 😎😎😎"

    # set up round feedback and output it user.
    #Add it to the game history list (include the round number
    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played + 1} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played += 1

    #if users are in infinite mode, increase the number of rounds
    if mode== "infinite":
        #can be wtv
        num_rounds += 1


# game loop ends here

# game history / statistics area

if rounds_played > 0:

    #calculate statistics
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = rounds_tied / rounds_played * 100

    print("📊📊📊 Game statistics 📊📊📊")
    print(f"Rounds played: {rounds_played} \t"
          f"Won: {percent_won:.2f}% \t"
          f"Lost: {percent_lost:.2f}% \t"
          f"Tied: {percent_tied:.2f}%")

    #ask if user wants game history
    want_game_history = string_checker("\nDo you want to see the game history?")

    if want_game_history == "yes":
        for item in game_history:
            print(item)

else:
    print("🐔🐔🐔 Oops - You chickened out! 🐔🐔🐔")