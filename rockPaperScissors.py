'''
Created on Feb 15, 2020

@author: ITAUser
'''

import random

keepPlaying = True

while(keepPlaying == True):
    print("Welcome, you ready to lose")
    print("First to 2 wins. Press q to quit. type in baby letters")
    #rock is 1, paper is 2, scissors is 3
   
    scoreComp = 0
    scorePlayer = 0
   
    while(scorePlayer < 2) and (scoreComp < 2):
        choiceComp = random.randint(1,3)
        choicePlayer = input("pick either rock, paper, or scissors!")
       
        if(choicePlayer == "q"):
            keepPlaying = False
            break
        elif((choicePlayer == "rock" ) and (choiceComp == 1)) or ((choicePlayer == "paper" ) and (choiceComp == 2)) or ((choicePlayer == "scissors" ) and (choiceComp == 3)):
            print("DRAAAW! (African Accent")
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
           
        elif((choicePlayer == "rock" ) and (choiceComp == 2)) or ((choicePlayer == "paper" ) and (choiceComp == 3)) or ((choicePlayer == "scissors" ) and (choiceComp == 1)):
            print("hold this for me real quick, it's an L, and you can keep it")
            scoreComp = scoreComp + 1
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
        elif((choicePlayer == "rock" ) and (choiceComp == 3)) or ((choicePlayer == "paper" ) and (choiceComp == 1)) or ((choicePlayer == "scissors" ) and (choiceComp == 2)):
            print("gg, you actually won, thats crazy")
            scorePlayer = scorePlayer + 1
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
        else :
            print("c'mon, you're smarter than this man. ROCK, PAPER, OR SCISSORS!")
           
    if (scorePlayer == 2):
            print("ok fine, you won, but i went easy on you...")
         
           
    if (scoreComp == 2):
            print("you will, never win against me")
           
    print("Computer's Score: ", + scoreComp , "Your Score: ", + scorePlayer)