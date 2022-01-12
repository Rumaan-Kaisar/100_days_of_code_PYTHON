vaLues = input("Enter the list of values : ").split()

for i in range(0, len(vaLues)):
    vaLues[i] = int(vaLues[i])

print(vaLues)

mAx = vaLues[0]

# Cannot use max()
for vAl in vaLues:
    if vAl > mAx :
        mAx = vAl

print(f"hihgest value : {mAx}")

# Shortest way: use the built-in function- max() 
print("Use the max() function : ", max(vaLues))

# python high.py