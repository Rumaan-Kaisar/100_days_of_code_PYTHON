
# # Creating/Declaring a class, Notice no "()"
# # Create a class named MyClass, with a property named x:
# class MyClass:
#   x = 5

# # creating object. Notice "()". calling constructor ?
# # Create an object named p1, and print the value of x:
# a_obj = MyClass()
# print(a_obj.x) # Accessing class properties in objects


class MyClass:
    def __init__(tb, a, b):
        # self referred to the object itself "MyClass"
        tb.a = a
        tb.b = b
        
    def my_func(mb):
        print(f"Yo babe you passed the {mb.b}")
    

a_obj = MyClass(3, 4)
a_obj.my_func() 

# python oop_class.py