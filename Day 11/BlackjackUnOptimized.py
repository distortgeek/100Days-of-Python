import random

cardDeck = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def blackJack():
    userDeck = []
    computerDeck = []
    sumUser = 0
    sumComputer = 0

    def cardDealer():
        for step in range(4):
            x = random.randint(0,len(cardDeck)-1)
            if len(userDeck) < 2:
                userDeck.append(cardDeck[x])
            else:
                computerDeck.append(cardDeck[x])

    def blackjackChecker():
        if sum(computerDeck) == 21:
            print(f"Computer won the game it's a Blackjack!\n Deck : {computerDeck},Total : {sum(computerDeck)}")
            quit()
        elif sum(userDeck) == 21:
            print(f"User won the game it's a Blackjack!\n Deck : {userDeck},Total : {sum(userDeck)}")
            quit()
        else:
            sumComputer = sum(computerDeck)
            sumUser = sum(userDeck)
        
        print(f"Your cards : {userDeck},current total: {sumUser}")
        print(f"Computer's first card : {computerDeck[0]}")

    def cardAdd():
        x = random.randint(0,len(cardDeck)-1)
        if cardDeck[x] == 11 and sum(userDeck > 21):
            userDeck.append(1)
        else:
            userDeck.append(cardDeck[x])
        x = random.randint(0,len(cardDeck)-1)
        if cardDeck[x] == 11 and sum(computerDeck > 21):
            computerDeck.append(1)
        else:
            computerDeck.append(cardDeck[x])
        
    def sumChecker():
        if sum(userDeck) > 21:
            print("------------------------------------------------")
            print(f"You Busted!Your cards : {userDeck},current total: {sum(userDeck)}")
            print(f"Computer won!")
            quit()
        elif sum(computerDeck) > 21:
            print("------------------------------------------------")
            print(f"Computer Busted!Computer's cards : {computerDeck},current total: {sum(computerDeck)}")
            print(f"User won!")
            quit()
        
    def compcardDraw():
        while sum(computerDeck) < 16:
            x = random.randint(0,len(cardDeck)-1)
            computerDeck.append(cardDeck[x])
                
    def result():
        if sum(userDeck) == sum(computerDeck):
            print("DRAW")
        elif sum(userDeck) > sum(computerDeck):
            print(f"You won! Your cards : {userDeck},current total: {sum(userDeck)}")
        elif sum(userDeck) < sum(computerDeck):
            print(f"Computer won! Computer's cards : {computerDeck},current total: {sum(computerDeck)}")

    print("Welcome to the Blackjack Game")
    playChoice = input("Do you want to play the game? (y/n): ").lower()
    if playChoice == "y":
        cardDealer()
        blackjackChecker()
        while True:
            continueChoice = input("Do you want to draw another card? (y/n): ").lower()
            if continueChoice == "y":
                cardAdd()
                sumChecker()
            else:
                compcardDraw()
                result()
                playAgain = input("Do you want to play again? (y/n): ").lower()
                if playAgain == "y":
                    blackJack()
                else:
                    quit()
    else:
        print("Have a great time! BYE!")
        quit()

blackJack()