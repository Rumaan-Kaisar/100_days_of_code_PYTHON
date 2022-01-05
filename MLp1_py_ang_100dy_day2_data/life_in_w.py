age = input("What is oue current age? :")
remaining_year = 90 - int(age)
remaining_month = remaining_year*12
remaining_week = remaining_year*52
remaining_day = remaining_year*365
message = f"If you live upto 90 years then you have remaining {remaining_year} years, or {remaining_week} weeks, or {remaining_month} months, or {remaining_day} days"
print(message)

