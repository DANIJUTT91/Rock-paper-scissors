
#-----------------ROCK_PAPER_SCISSORS---------------------#

def pState(uState):
    if uState == "s" or uState == "S" or uState == "Scissors" or uState == "scissors" or uState == "SCISSORS":
        uState = "s"
        print("Player: Scissors")
    elif uState == "r" or uState == "R" or uState == "Rock" or uState == "rock" or uState == "ROCK":
        uState = "r"
        print("Player: Rock")
    
    elif uState == "P" or uState == "p" or uState == "Paper" or uState == "paper" or uState == "PAPER":
        uState = "p"
        print("Player: Paper")
    else:
        uState = "I"
        print("Invalid")
    return uState
   
def cState():
    i = random.randint(1,3)
    if i==1:
        compstate = "r"
        print("Computer: Rock")
    elif i==2:
        compstate = "p"
        print("Computer: Paper")
    elif i==3:
        compstate = "s"
        print("Computer: Scissors")
    else:
        compstate = "I"
        print("Error")
    return compstate

def playerWin(com,player):
    if com == "p" and player == "s" or com == "r" and player == "p" or com == "s" and player == "r":
        return True
    else:
        return False


pCount = 0
cCount = 0
while 1:
    print("------Rock - Paper - Scissors------")
    playerState = ""
    compState = ""    
    playerState = input("Enter your choice:\nP-Paper\nR-Rock\nS-Scissors\nE-Exit\n")
    print("")
    if playerState != "e" and playerState != "E" and playerState != "exit" and playerState != "Exit" and playerState != "EXIT":
        playerState = pState(playerState)
        if(playerState == "I"):
            break
        compState = cState()
    else:
        print("---EXIT---")
        break

    if compState == "I" or playerState == "I":
        break
    elif compState == playerState:
        print("\n*Tie*")
        pCount+=1
        cCount+=1
    else:
        
        if playerWin(compState,playerState):
            pCount+=1
            print("\n*Player Won*")
        else:
            cCount+=1
            print("\n*Computer won*")
            
    print("\nComputer's Score = " + str(cCount) + " | Player's Score = " + str(pCount) + " \n\n\n")
print("\nResults:\n\tComputer's Score = " + str(cCount) + "\n\tPlayer's Score = " + str(pCount))
if pCount != 0 or cCount != 0:
    print("\n\tYou WON!!") if pCount>cCount  else print("\n\tYou LOST!!")

