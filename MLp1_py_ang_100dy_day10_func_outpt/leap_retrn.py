
    
def is_Leap(yer):
    if yer%4 == 0:    
        if yer%100 == 0:
            if yer%400 == 0 :
                print("\t\t Is a Leapaa Year \n\n")
                return "Leap"
            else:
                print("\t\t Oh no!! Not Leap Year \n\n")
                return "NotLeap"
        else:
            print("\t\t Is a Leap Year \n\n")
            return "Leap"
    else:
        print("\t\t Not a Leap Year \n\n")
        return "NotLeap"


 
def days_in_month(yr, mNth):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if is_Leap(yr) == "Leap":
        month_days[1] = 29
    return f"\nEntered month {mNth} of year {yr} has {month_days[mNth - 1]} days\n"



#Do NOT change any of the code below

year = int(input("\t\tEnter the year ? "))
month = int(input("Enter a month: ")) 

days = days_in_month(year, month) 
print(days)

# python leap_retrn.py