number = int(input("Enter the number: "))

def prMchk(num) : 
    is_prm = True
    fc = 0
    for i in range(2, int(num/2)):
        if (num % i) == 0 :
            is_prm = False
            fc = i

    if is_prm == True :
        print(f"\t{num} is a prime number")
    else :
        print(f"\t{num} isn't prime. Divisible by {fc}")

for k in range(2, number+1):
    prMchk(k)

# python prime.py