import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
'''

print(logo)

bidders_data_list = []

while True:
    
    def details(name,bid):
        bidders_data_dict = {}
        bidders_data_dict[name]= bid
        bidders_data_list.append(bidders_data_dict)
        return None
    
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $"))
    
    details(name = name,bid = bid)
    
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no' : ").lower()
    if more_bidders == "yes":
        os.system("cls")
        continue
    else:
        print(bidders_data_list)
        winner_name = ""
        winner_bid = 0
        for i in bidders_data_list:
            for key,value in i.items():
                if value > winner_bid:
                    winner_name = key
                    winner_bid = value
        os.system("cls")
        print("Congratulations!!")
        print(f"The winner is {winner_name} with a bid of ${winner_bid}")
        quit()