# game.py

#Importing all necessary modules and packages
import random
from dotenv import load_dotenv
import os


#Creating the list of options for further reference
options = ["Rock","Paper","Scissors"]

# Pulling the username info from .env and using it in the welcome message
load_dotenv()
usname = os.getenv("USER_NAME")
message = f"Welcome to the game, {usname}!"
print(message)

#Getting the inputs from the user
game = input("To play the game, please enter Rock, Paper or Scissors here: ")
game = game.title()

#Validating the inputs
if game == "Rock" or game == "Paper" or game == "Scissors":
    print("The input is valid. You selected ",game)
else:
    print("The input is incorrect, exiting")
    exit()

#Generating computer's choice from the list of options
comp = random.choice(options)
print("Computer selected: ",comp)

#In this section we determine the winner by sending the program through a nested set of IF
#statements. The idea is to make sure the program doesn't have to go through each and every
#IF statement for all 9 potential outcomes, and only goes through one "branch" of the
#conditional. This should help with calculating the results faster.
#When the program goes through the conditionals, it determines if the player won (x=1),
#lost (x=-1) or if it's a draw (x=0).
if game == "Rock":
    if comp == "Rock":
        x = 0
    elif comp == "Scissors":
        x = 1
    else: x = -1
elif game == "Paper":
    if comp == "Paper":
        x = 0
    elif comp == "Rock":
        x = 1
    else: x = -1
else:
    if comp == "Scissors":
        x = 0
    elif comp == "Paper":
        x = 1
    else: x = -1

#Now that we know the result (x being -1, 1, or 0), we can generate the outcome message.
#By using this second IF statement we reduce "wordiness" of the code because we don't need
#to have those Print statement at every outcome above - we only list them once here.
if x == 0:
    print("Draw!")
elif x == -1:
    print("You lost, try again")
else: print("You won! Congrats")

#The game is over and it's time to say goodbye.
message = f"It was a great game, {usname}, please play again!"
print(message)