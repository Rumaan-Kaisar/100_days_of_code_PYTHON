
# python has dynamic type property and also Python is strongly typed

# But we can also make variable type hint by using "type-hint". It dont make it static

age = 12
age = "ypung"

# but if we use "type-hint" the type will be shown by a hint, anywhere of the code

hour: int

hour = 23

print(f"age: {age}, hour: {hour}")


# we can use "type-hint" in a for function PARMS/INPUT function declarations
# so that if we use that function anwhere in the code, the type will be shown by "hint"
def samp(a: int):
    print(a)


# other codes
# other codes
# other codes
# other codes
# other codes

samp(44)

# we can also use "type-hint" for function OUTPUT in a function declarations
# so that if we use the result of the function anwhere in the code, the OUTPUT-type will be shown by "hint"
def nOsamp(a: int) -> int:
    print(a)
    return a


# other codes
# other codes
# other codes
# other codes
# other codes

nOsamp()

# python type_hint.py