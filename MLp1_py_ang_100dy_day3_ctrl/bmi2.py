weight = int(input("\t\tEnter the weight : "))
height = int(input("\t\tEnter the height : "))

bmi = round(weight/(height**2))

if bmi < 18.5 : 
    print(f"\n\t Your BMI is {bmi}, you are Underweight \n\n")
elif 18.5 <= bmi < 25:
    print(f"\n\t Your BMI is {bmi}, you are Normal weight \n\n")
elif 25 <= bmi < 30:
    print(f"\n\t Your BMI is {bmi}, you are Overweight \n\n")
elif 30 <= bmi < 35:
    print(f"\n\t Your BMI is {bmi}, you are Obese \n\n")
else :
    print(f"\n\t Your BMI is {bmi}, you are Clinically Obese \n\n")