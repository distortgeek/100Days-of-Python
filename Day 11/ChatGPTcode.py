import random

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

def draw_card():
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])

def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

def check_blackjack(hand):
    return len(hand) == 2 and calculate_score(hand) == 21

def check_bust(hand):
    return calculate_score(hand) > 21

def playGame():
    print(logo)
    while True:
        userDeck = [draw_card(), draw_card()]
        compDeck = [draw_card(), draw_card()]

        print(f"Your deck: {userDeck}, current total: {calculate_score(userDeck)}")
        print(f"Comp's card : {compDeck[0]}")

        if check_blackjack(userDeck):
            print("Congrats you won! Blackjack!")
        else:
            while calculate_score(userDeck) < 21:
                moreCards = input("Do you want to draw more cards? (y/n) : ").lower()
                if moreCards == "y":
                    userDeck.append(draw_card())
                    print(f"Your deck: {userDeck}, current total: {calculate_score(userDeck)}")
                else:
                    break
            
            if check_bust(userDeck):
                print("You Lose! You busted!")
            else:
                while calculate_score(compDeck) < 17:
                    compDeck.append(draw_card())
                print(f"Comp's deck: {compDeck}, current total: {calculate_score(compDeck)}")
                
                if check_bust(compDeck):
                    print("Comp Lose! Computer busted!")
                else:
                    user_score = calculate_score(userDeck)
                    comp_score = calculate_score(compDeck)
                    
                    if user_score == comp_score:
                        print("Draw!")
                    elif user_score > comp_score:
                        print("You Win!")
                    else:
                        print("Computer Wins!")
        
        playAgain = input("Do you want to play again? (y/n): ").lower()
        if playAgain != "y":
            print("Thanks for playing!")
            break

# Start the game
if __name__ == "__main__":
    playGame()
