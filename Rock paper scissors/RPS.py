# Rock paper scissors game
import random

scoreH = 0
scoreC = 0

def rock():
    global scoreH
    global scoreC
    list = ["Rock", "Paper", "Scissors"]
    rockChoice = random.choice(list)
    if rockChoice == "Rock":
        print("\nComputer chose rock")
        print("Draw")
        print(str(scoreH) + "-" + str(scoreC))
    elif rockChoice == "Paper":
        print("\nComputer chose paper")
        print("You lose!")
        scoreC = scoreC + 1
        print(str(scoreH) + "-" + str(scoreC))
    elif rockChoice == "Scissors":
        print("\nComputer chose scissors")
        print("You win!")
        scoreH = scoreH + 1
        print(str(scoreH) + "-" + str(scoreC))

def paper():
    global scoreH
    global scoreC
    list = ["Rock", "Paper", "Scissors"]
    rockChoice = random.choice(list)
    if rockChoice == "Rock":
        print("\nComputer chose rock")
        print("You win!")
        scoreH = scoreH + 1
        print(str(scoreH) + "-" + str(scoreC))
    elif rockChoice == "Paper":
        print("\nComputer chose paper")
        print("Draw")
        print(str(scoreH) + "-" + str(scoreC))
    elif rockChoice == "Scissors":
        print("\nComputer chose scissors")
        print("You lose!")
        scoreC = scoreC + 1
        print(str(scoreH) + "-" + str(scoreC))

def scissors():
    global scoreH
    global scoreC
    list = ["Rock", "Paper", "Scissors"]
    rockChoice = random.choice(list)
    if rockChoice == "Rock":
        print("\nComputer chose rock")
        print("You lose!")
        scoreC = scoreC + 1
        print(str(scoreH) + "-" + str(scoreC))
    elif rockChoice == "Paper":
        print("\nComputer chose paper")
        print("You win!")
        scoreH = scoreH + 1
        print(str(scoreH) + "-" + str(scoreC))
    elif rockChoice == "Scissors":
        print("\nComputer chose scissors")
        print("Draw")
        print(str(scoreH) + "-" + str(scoreC))

def mainMenu():
    print("1 - Rock\n2 - Paper\n3 - Scissors")
    mChoice = int(input("Enter: "))
    if mChoice == 1:
        rock()
    elif mChoice == 2:
        paper()
    elif mChoice == 3:
        scissors()
    else:
        print("Error")
        mainMenu()

def scoreHuman(human):
    human = human + 1


run = True
while run == True:
    mainMenu()

