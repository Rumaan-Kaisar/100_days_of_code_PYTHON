#Calculator
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


#Add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Devide
def devide(n1, n2):
    if(n2>0):
        return n1 / n2
    else:
        return "undefined"

operations = {"+" : add, "-" : subtract, "*" : multiply, "/" : devide}

def calculator():
    print(logo)
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))

    eXit = False
    while not eXit:
        for op in operations:
            print(op)
        oPr = input("\n\t Pick an operation from above : ")

        result = operations[oPr](num1, num2)
        print(f"\n\t{num1} {oPr} {num2} = {result}\n")

        aSk = input(f"""Type \'ex\' to end or \'bg\' to satrt again. 
                    Press enter/other-key to cintinue with result {result}""")
        if aSk == "ex":
            eXit = True
        elif aSk == "bg":
            calculator()
            eXit = True
        else:
            num2 = float(input("Enter another number : "))
            num1 = result

calculator()

# python calculator_pt_1.py