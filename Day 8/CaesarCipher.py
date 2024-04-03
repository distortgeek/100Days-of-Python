alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)
print("Welcome to the Cipher Tool!")
while True:
    def encrypt(text,shift):
        cipher_text = ""
        for letter in text:
            if letter in alphabet:
                index = alphabet.index(letter)
                cipher_text += alphabet[(index + shift)%26]
            else:
                cipher_text += letter
            
        return(cipher_text)
        
    def decrypt(text,shift):
        decipher_text = ""
        for letter in text:
            if letter in alphabet:
                index = alphabet.index(letter)
                decipher_text += alphabet[(index - shift)%26]
            else:
                decipher_text += letter
        return(decipher_text)
    
    def get_details():
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if direction == 'encode':
            print(f"Here's the decoded result : {encrypt(text=text,shift=shift)}")
            repeat = input("Type 'yes' if you want to go again.Otherwise type 'no'.").lower()
            if repeat == "yes":
                get_details()
            else:
                quit()
        elif direction == 'decode':
            print(f"Here's the decoded result : {decrypt(text=text,shift=shift)}")
            repeat = input("Type 'yes' if you want to go again.Otherwise type 'no'.").lower()
            if repeat == "yes":
                get_details()
            else:
                quit()
        else:
            print("Invalid input. Please try again.")
    
    get_details()