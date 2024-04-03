print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? : "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age in years? : "))
    if age >= 18:
        wants_photo = input("Do you want a photo taken? Y or N. : ")
        if wants_photo == "Y" or wants_photo == "y":
            print("Please pay $15.")
        else:
            print("Please pay $12.")
    elif age <= 12:
        wants_photo = input("Do you want a photo taken? Y or N. : ")
        if wants_photo == "Y" or wants_photo == "y":
            print("Please pay $8.")
        else:
            print("Please pay $5.")
    else:
        wants_photo = input("Do you want a photo taken? Y or N. : ")
        if wants_photo == "Y" or wants_photo == "y":
            print("Please pay $10.")
        else:
            print("Please pay $7.")
else:
    print("Sorry,you have to grow taller before you can ride the rollercoaster!")
