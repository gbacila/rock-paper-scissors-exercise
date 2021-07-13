# game.py
import random
options = ["Rock","Paper","Scissors"]
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