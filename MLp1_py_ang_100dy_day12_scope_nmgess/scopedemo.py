# There is no block-scope in py
# Scope remains same in all Kind of while, for, if CTRL statemnt
t = 10
if t < 34 :
    p = 45

# variable p can be accessed outside "if" block
print(p)


def out_scope():
    local_var = 123
    print(local_var)

# follwing throws error
# print(local_var)

# Global variables can be accessed and modified within function by keyword "global"
# BUT not a good idea. Instead "return" stmnt should use

glbl_var = 100

def crazy_scope():
    # Following looks for the specified global variable outside current scope
    global glbl_var
    glbl_var = 300

print(f"Original global variable : {glbl_var}")
crazy_scope()
print(f"after function call global variable : {glbl_var}")


# Identical named local-global
test_var = 700
def scope_demo2():
    test_var = 100
    print("Inside funtion", test_var)

scope_demo2()
print("Outside funtion", test_var)

# Global variables are good for constants. Can be used in "local scope"
# Coveentionally Upper-case letters are used for constants.  Eg:
PI = 3.14159
HTTP = "https://google.com"

def local_demo():
    t= PI/2.0
    return f"Pi : {PI} and 1/2 Pi: {t}"
print(local_demo())

# python scopeDemo.py