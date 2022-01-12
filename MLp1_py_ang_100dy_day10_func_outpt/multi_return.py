# Name converter to Title- case

def TitLizer(firstName, lastName):
    if (firstName == '') or (lastName == ''):
        return f"No Empty Name"
    fNm = firstName.title()
    lNm = lastName.title()
    return f"{fNm} {lNm}"


print(f"\n\t\t{TitLizer(input('Enter first-name : '), input('Enter last-name : '))}")

# python multi_return.py