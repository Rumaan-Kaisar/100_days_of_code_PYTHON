print("\n\t\tWelcome to the rollercoster !!!")
height = int(input("\t\tWhat is your height in cm ? "))

bill = 0

# Notice the "indent". It is very inportant in PYTHON 
if height < 120 : 
    print("\t\t Sorry you can't ride :( \n\n")
else:
    age = int(input("\t\tWhat is your age ? "))
    if age >= 18 :
        bill = 12
        print("\t\t Go ahed !! Buy ticket from the counter with $12. Enjoy !!! \n\n")
    elif 9 <= age < 18 :
        bill = 7
        print("\n\t\t Go ahed !! Buy ticket from the counter with $7. Enjoy !!!  \n\n")
    else :
        bill = 5
        print("\t\t Where is you Mama ?? \n\t\t Go ahed !! Buy ticket from the counter with $5. Enjoy !!!  \n\n")
    
    want_photo = input("\t\tWant a photo ? y / n :")
    if want_photo == 'y':
        bill += 3
    print(f"your Bill is : {bill}")
    