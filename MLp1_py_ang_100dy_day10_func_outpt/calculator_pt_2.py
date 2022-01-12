#Calculator

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))


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

for op in operations:
    print(op)
oPr = input("\n\t Pick an operation from above : ")


result = operations[oPr](num1, num2)
print(f"\n\t{num1} {oPr} {num2} = {result}\n")

# python calculator_pt_1.py