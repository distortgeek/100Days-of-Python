import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cardDeck = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def playGame():
    userDeck = []
    compDeck = []

    gameOver = True
    def cardDraw():
        card = random.choice(cardDeck)
        return card

    def cardDistribution():
        for step in range(2):
            userDeck.append(cardDraw())
            compDeck.append(cardDraw())
            
    def cardAdd(x):
        y = cardDraw()
        if y == 11 and sum(x) > 21:
            x.append(1)
        else:
            x.append(y)
            
    def userCards():
        if sum(userDeck) == 21:
            return 1
        elif sum(userDeck) > 21:
            return 0
        
    def compCards():
        if sum(compDeck) == 21:
            return 1
        elif sum(compDeck) > 21:
            return 0
        
    def decision():
        if userCards() == 1:
            print("Congrats you won! Blackjack!")
            return False
        elif compCards() == 1:
            print("Computer Won! Blackjack!")
            return False
        elif userCards() == 0:
            print("You Lose!")
            return False
        elif compCards() == 0:
            print("Comp Lose!")
            return False
        elif sum(userDeck) == sum(compDeck):
            print("Draw!")
            return False
            
    print(logo)
    gameStart = input("Do you want to play blackjack?(y/n) : ").lower()
    if gameStart == "y":
        while gameOver:
            cardDistribution()
            print(f"Your deck: {userDeck},current total: {sum(userDeck)}")
            print(f"Comp's card : {compDeck[0]}")
            if sum(compDeck) == 21 or sum(userDeck) == 21 and sum(compDeck) == 21:
                print("Computer Won! Blackjack!!!")
                gameOver = False
            else:
                while gameOver:
                    if userCards() == 1:
                        print("Congrats you won! Blackjack!")
                        gameOver = False
                    elif compCards() == 1:
                        print("Computer Won! Blackjack!")
                        gameOver = False
                    elif userCards() == 0:
                        print("You Lose! You busted!")
                        gameOver = False
                    elif compCards() == 0:
                        print("Comp Lose! Computer busted!")
                        gameOver = False
                    moreCards = input("Do you want to draw more cards? (y/n) : ").lower()
                    if moreCards == "y":
                        cardAdd(userDeck)
                        cardAdd(compDeck)
                        print(f"Your deck: {userDeck},current total: {sum(userDeck)}")
                        print(f"Comp's card : {compDeck[0]}")
                        if userCards() == 1:
                            print("Congrats you won! Blackjack!")
                            gameOver = False
                        elif compCards() == 1:
                            print("Computer Won! Blackjack!")
                            gameOver = False
                        elif userCards() == 0:
                            print("You Lose! You busted!")
                            gameOver = False
                        elif compCards() == 0:
                            print("Comp Lose! Computer busted!")
                            gameOver = False
                        else:
                            continue
                    else:
                        while gameOver:
                            if sum(compDeck) < 17 :
                                cardAdd(compDeck)
                            else:
                                y = decision()
                                gameOver = y
        playAgain = input("Do you want to play again? (y/n): ").lower()
        if playAgain == "y":
            os.system("cls")
            playGame()
        else:
            quit()