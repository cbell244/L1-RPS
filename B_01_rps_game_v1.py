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



# main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]


print("🪨📃✂️ Rock / Paper / Scissors Game ✂️📃🪨")
print()

# asl user if they want to see te instructons and display them if requested
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

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("You chose", user_choice)

    #check if user inputs exit code
    if user_choice == "xxx":
        break

    rounds_played += 1

    #if users are in infinite mode, increase the number of rounds
    if mode== "infinite":
        #can be wtv
        num_rounds += 1


# game loop ends here

# game history / statistics area