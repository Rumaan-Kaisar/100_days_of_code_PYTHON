import random
 
sequence = [random.randint(0, i) for i in range(10)]

# Notice the '+'  not used. Instead the output is sent as parameter
print('Before shuffling the random sequence : ', sequence)

# Applying shuffle()
random.shuffle(sequence)
print('After shuffling', sequence)





# python ranmeth.py