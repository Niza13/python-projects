# Rock-Paper-Scissor


import random

choices = ["rock", "paper", "scissor"]

chances=5

for i in range(chances):

    computer = random.choice(choices)
    player = None

    player = input("Enter Rock Papaer or Scissor:").lower()

    if(player==computer):
        print("computer  player")
        print(computer,"\t",player)
        print("Tie!")
        chances = chances-1

    elif(player=="rock"):
        if(computer=="paper"):
            print("computer  player")
            print(computer,"\t",player)
            print("computer wins")
            chances = chances-1
        else:
            print("computer  player")
            print(computer,"\t",player)
            print("player wins")
            chances = chances-1

    elif(player=="paper"):
        if(computer=="scissor"):
            print("computer  player")
            print(computer,"\t",player)
            print("computer wins")
            chances = chances-1
        else:
            print("computer  player")
            print(computer,"\t",player)
            print("player wins")
            chances = chances-1

    elif(player=="scissor"):
        if(computer=="rock"):
            print("computer  player")
            print(computer,"\t",player)
            print("computer wins")
            chances = chances-1
        else:
            print("computer  player")
            print(computer,"\t",player)
            print("player wins")
            chances = chances-1

    else:
        print("enter valid choice")

print("Game Ended")