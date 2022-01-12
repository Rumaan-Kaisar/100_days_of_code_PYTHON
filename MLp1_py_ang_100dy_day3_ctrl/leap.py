yer = int(input("\t\tEnter the year ? "))

if yer%4 != 0 : 
    print("\t\t Not a Leap Year \n\n")
elif yer%4 == 0:
    if yer%100 != 0 :
        print("\t\t Is a Leap Year \n\n")
    elif yer%100 == 0:
        if yer%400 == 0 :
            print("\t\t Is a Leapaa Year \n\n")
        else:
            print("\t\t Oh no!! Not Leap Year \n\n")
