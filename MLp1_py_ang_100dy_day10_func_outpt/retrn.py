# Name converter to Title- case

def TitLizer(firstName, lastName):
    """Takes first-Name and last-Name as string and returns Title-Case string format"""
    
    # above statement is a Dockstring
    
    fNm = firstName.title()
    lNm = lastName.title()
    return f"{fNm} {lNm}"

formattedName = TitLizer("KurE", "SaTler")
print(formattedName)

print(f"\n\t\t{TitLizer('PiLLI', 'soSo')}")

TitLizer()

# python retrn.py