print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n$"))
tip = float(input("What percentage tip would you like to give?\n"))
people = int(input("How many people to split bill?\n"))
print(f"Each person should be pay:${round((bill/people)+(bill/people)*(12/100),2)}")

