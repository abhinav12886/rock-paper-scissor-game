import random

#defining functions...

def Rock():
    if user_choice1 == "r":
        if computer_choice == "s":
            print("you won , computer chose : scissors", (computer_choice))
        else:
            print("you lose ,computer chose paper : ",(computer_choice))
        #else:
         #   print("it is a tie")

    else:
        print("it is a tie")
    
def Scissors():
    if user_choice1 == "s":
        if computer_choice == "r":
            print("you lose , computer chose : rock : ",(computer_choice))
        else:
            print("you won , computer chose paper : ",(computer_choice))
    else:
        print("it is a tie")

def Paper():
    if user_choice1 == "p" :
        if computer_choice == "r" :
            print("you won . computer chose : rock : " ,(computer_choice))
        else:
            print("you lose , computer chose scissors : ",(computer_choice))
    else:
        print("it is a tie")
    
while True :

    #taking user choice as input ...

    print("select your choice among :- (r) for rock / (p) for paper / (s) for scissors :  ")
    user_choice = input()
    user_choice1 = user_choice
    user_choice1 = user_choice1.lower()
    user_choice1 = user_choice1[0]
    computer_actions = ("r","p","s")
    computer_choice = random.choice(computer_actions)

    if user_choice1 == computer_choice:
        print("both chose the same ",user_choice ,"it is a tie")
        
    elif user_choice1 == "r":
        Rock()

    elif user_choice1 == "p":
        Paper()

    else:
        Scissors()

    play_more = input("if you want to play more type y for yes  else type n for no ")
    if play_more.lower() != "y" :
        break
        
            
