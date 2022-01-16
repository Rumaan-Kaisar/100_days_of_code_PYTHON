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


def calculate(**kWArgs):
    print(kWArgs)
    # Acessing kwargs argumnets
    for (key, value) in kWArgs.items():
        print(key)
        print(value)
    
    # Acessing Specific kwargs argumnet
    print(kWArgs["sum"])

calculate(sum = 8, multiply = 9)


# **kwargs in class-objects. create class with optional keyword arguments
class mycar:
    def __init__(self, **kw):
        # self.maker = kw["make"]
        # self.carName = kw["model"]
        # using get() insted of [] makes the aguments varible. kwarg.get("key")
        # So if any of these arguments misses no error wil arise. Returns None instead
        self.maker = kw.get("make")
        self.carName = kw.get("model")

car = mycar(make= "Nissan", model = "GT-8")
print(car.carName)
car2 = mycar(make= "Paganni")
print(f"maker : {car2.maker} and model : {car2.carName}")
# python kw_arg.py