# parent class
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def brethe(self):
        print("Inhale Exhale.")


# child class
class Fish(Animal):
    def __init__(self):
        super().__init__() # call __init__() of parent-class

    def swim(self):
        print("Moving in the water")

    # modifying parent-class's method
    def brethe(self):
        # loading parent's method
        super().brethe()
        print("Doing this underwater.")



# creating object of child-class. 
# Also contain the prperties & methods of parent class
nemo = Fish()
nemo.swim()

# Accessing parent-class properties and methods
print("No. of eyes : ", nemo.num_eyes)
nemo.brethe()

# python inheritance_demo.py