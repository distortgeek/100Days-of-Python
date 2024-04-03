import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''



stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6

display = []
word_list = [
    "Samosa", "Vada Pav", "Pav Bhaji", "Pani Puri", "Bhel Puri","Dahi Puri", "Aloo Tikki", "Chole Bhature", "Sev Puri", "Papdi Chaat","Raj Kachori", "Kachori", "Batata Vada","Dabeli", "Misal Pav","Ragda Pattice", "Dhokla", "Khaman", "Mirchi Bajji", "Onion Pakoda","Paneer Tikka", "Chicken Tikka", "Chicken 65", "Chicken Lollipop","Tandoori Chicken", "Chicken Shawarma", "Egg Roll", "Kathi Roll","Paneer Roll", "Aloo Chaat","Tandoori Momos", "Paneer Momos","Chicken Momos", "Veg Manchurian", "Chicken Manchurian", "Gobi Manchurian","Chicken Chilli", "Veg Hakka Noodles", "Egg Hakka Noodles","Chicken Hakka Noodles", "Veg Spring Roll", "Egg Spring Roll","Chicken Spring Roll", "Veg Frankie", "Egg Frankie", "Chicken Frankie","Veg Burger", "Egg Burger", "Chicken Burger", "Pizza"
]

chosen_word = word_list[random.randint(0, len(word_list)-1)].lower()

word_length = len(chosen_word)

for _ in range(word_length):
    display.append("_")
    
print(logo)
    
while True:
    guess = input("Guess the letter : ").lower()

    if guess in chosen_word:
        for index in range(word_length):
            if guess == chosen_word[index]:
                display[index] = guess
        print("Your guess was right")
    
    elif lives == 0:
            print(stages[lives])
            print(f"Game Over. The correct word was{chosen_word}")
            exit()
    
    else:
        print(stages[lives])
        lives -= 1

    print(display)

    for index in range(word_length):
        if '_' in display:
            continue
        else:
            print("Congrats! You guessed the word " + chosen_word)
            exit()
