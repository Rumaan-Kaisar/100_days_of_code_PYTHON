row1 = ["o", "o", "o"]
row2 = ["o", "o", "o"]
row3 = ["o", "o", "o"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where you want to put your treasure ? : row-col ")

slct_row = map[int(position[0])-1]
slct_row[int(position[1])-1] = "x"

# or we can access directly as 2-d array as a[m][n]
print(f"{map[1][2]}")
hrz = int(position[0])-1
vert = int(position[1])-1
map[hrz][vert] += "D"

print(f"{row1}\n{row2}\n{row3}")

# python trasure_map.py