total = input("What was the total bill? : $")
percentage = input("What parcentage tip ypu like to give? 0, 10, 12, or 15 ? :")
split = input("How many people you want to split the bill? :")

payTotal = float(total) + (float(percentage)/100.0)*float(total)
finalPayment = round(payTotal/int(split), 2)
print(f"Each person should pay: ${finalPayment}")

# to inspect formatting works : use $150  with 12% splitted to 5
formatted = "{:.2f}".format(finalPayment)
print(f"Each person should pay (Formatted): ${formatted}")

