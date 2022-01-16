def add(*arGs):
    print(arGs) # returns a tuple "which are the inputs"
    # So we can access them as Index
    print(f"first argument is {arGs[0]}")
    sum = 0
    for n in arGs:
        print(n)
        sum += n
    
    return sum



print(f"Sum is : {add(1, 2, 3)}")

# python playground.py