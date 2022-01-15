# practiced version
with open("file1.txt") as file1:
    file1_data = file1.readlines()
    with open("file2.txt") as file2:
        file2_data = file2.readlines()
        common = [int(item.strip()) for item in file1_data if (item in file2_data)]
        print(common)

print(common)

# instructor solution
with open("file1.txt") as file1:
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()

common_2 = [int(num) for num in file1_data if (num in file2_data)]

print("Instructor version : ",common_2)



# python two_file_common_num.py