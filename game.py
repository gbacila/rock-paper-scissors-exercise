# game.py
import random
from dotenv import load_dotenv
import os
options = ["Rock","Paper","Scissors"]

load_dotenv()
print(os.getenv("SECRET_MESSAGE"))

#Getting the user name. Found at https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
usname = os.getenv("USER_NAME")
print(usname)

print("Welcome to the game, ",usname,"!")
print("Rock, Paper, Scissors, Shoot!")
#Getting the user's inputs
game = input("Please enter Rock, Paper or Scissors here: ")

#Checing the inputs
if game == "Rock" or game == "Paper" or game == "Scissors":
    print("The player selected ",game)
else:
    print("The input is incorrect, exiting")
    exit()

comp = random.choice(options)
print("Computer selected: ",comp)

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
if x == 0:
    print("Draw!")
elif x == -1:
    print("You lost, try again")
else: print("You won! Congrats")

print("It was a great game, ",usname,", Please play again!")
