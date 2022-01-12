class User:
    pass

user_1 = User()

user_1.nAm = "Beluga"
user_1.id = "001"

print(user_1.nAm)
print(user_1.id)

class InitClasDemo:
    def __init__(self, v1, v2, v3):
        self.ver1 = v1
        self.mult = v2*v3

test_obj = InitClasDemo(1, 2, 3)
print("multiple is :", test_obj.mult)

# python class_demo.py