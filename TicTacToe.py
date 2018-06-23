'''
Enjoy your favurite tic tac toe game with your friend.
The code is inspired by The BillingTon
http://thebillington.co.uk/blog/posts/writing-a-tic-tac-toe-game-in-python
Slighlty improved by Arihant-Sai

'''

import os
def printBoard(choices,warning):
    osname = os.name
    if(osname == "nt"):
        os.system("cls")
    elif(osname == "posix" or osname == "mac"):
        os.system("clear")
    
    if warning:
        print(warning,end="\n")
    print("\nPlayer One : X, Player Two : O",end="\n\n")

    #first row
    print("   |   |   ",sep="",end="\n")
    print(" ",choices[0]," |"," ",choices[1]," |"," ",choices[2],sep="",end="\n")# choicess needs to be printed here
    print("   |   |   ",sep="",end="\n")
    print("-------------",end="\n")
    
    #second row
    print("   |   |   ",sep="",end="\n")
    print(" ",choices[3]," |"," ",choices[4]," |"," ",choices[5],sep="",end="\n")# choicess needs to be printed here
    print("   |   |   ",sep="",end="\n")
    print("-------------",end="\n")
    
    #third row
    print("   |   |   ",sep="",end="\n")
    print(" ",choices[6]," |"," ",choices[7]," |"," ",choices[8],sep="",end="\n")# choicess needs to be printed here
    print("   |   |   ",sep="",end="\n")


def isGameOver(choices):
    for x in range(0,3):
        y = x*3
        
        # for rows
        if((choices[y]!= " ") and (choices[y]==choices[y+1]) and (choices[y]==choices[y+2])):
            #printBoard(choices)
            return True
        
        # for columns
        if((choices[x]!= " ") and (choices[x]==choices[x+3]) and (choices[y]==choices[x+6])):
            #printBoard(choices)
            return True
    
    # for primary diagonal
    if((choices[0]!= " ") and (choices[0]==choices[4]) and (choices[0]==choices[8])):
        #printBoard(choices)
        return True
    
    # for secondary diagonal
    if((choices[2]!= " ") and (choices[2]==choices[4]) and (choices[2]==choices[6])):
        #printBoard(choices)
        return True

    return False


playerOneName = input(">> Player One Name : ")
playerTwoName = input(">> Player Two Name : ")
choices = []
winner = False
playerOne = True
warning = None

for x in range(0,9):
    choices.append(" ")


while not winner:
    printBoard(choices,warning)
    print("Valid choices (1-9)")
    choice = None
    if playerOne:
        choice = int(input(">> "+playerOneName+" : "))
    else:
        choice = int(input(">> "+playerTwoName+" : "))

    if(not (choice>=1 and choice<=9)):
        warning  = "\nNot a valid move" 
        continue
    if(choices[choice-1] != " "):
        warning  = "\nMove already has been played"
        continue
    if playerOne:
        choices[choice-1] = "X"
    else:
         choices[choice-1] = "O"

    if(not isGameOver(choices)):
        playerOne = not playerOne
        warning = None
        continue
    else:
        winner = True
        continue

printBoard(choices,None)
if playerOne:
    print(playerOneName+" nails it")
else:
    print(playerTwoName+" nails it")