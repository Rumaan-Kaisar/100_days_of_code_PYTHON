# followinh wil be splitted with respect to space
# usnig split() with input() directly will generate a list
student_height = input("Enter the list of students height : ").split()

for i in range(0, len(student_height)):
    student_height[i] = int(student_height[i])

print(student_height)

sum_1 = 0
count = 0

# Don't change code above

# Cannot use len() or sum()
for n in student_height:
    sum_1 += n
    count += 1

average = round(float(sum_1)/float(count), 3)

print("Average of the given lengths : ", average)

# Shortest way: use the sum() function and len() 
print("Use the sum() and len() : ", sum(student_height)/len(student_height))


# python avg_higt.py