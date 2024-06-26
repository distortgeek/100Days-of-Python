logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {"+":add, "-": subtract,"/": divide,"*": multiply}

num1 = float(input("What is the first number : "))
num2 = float(input("What is the second number : "))

def operation(num1,num2):
    for i in operators:
            print(i)

    operations_symbol = input("Pick an operation from the line above : ")
    operator_name = operators[operations_symbol]
    result = operator_name(num1,num2)
    print(f"{num1} {operations_symbol} {num2} = {result}")
    return result

x = operation(num1,num2)

while True:
    loop_choice = input("Do you want to do more operations on this number? (y/n): ").lower()
    if loop_choice == "y":
        print(f"Your result is the first number which is : {x}")
        num3 = float(input("Enter the second number to perform the operation : "))
        x = operation(x, num3)
    else:
        print(f"Your final result is : {x}")
        quit()