# create a new dictionary from a list

import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie' ]
student_random_score = {nam : random.randint(60, 89) for nam in  names }
print(student_random_score)

# create a new dictionary from a dictionary
passed_students = {nam : score for (nam, score) in student_random_score.items() if (score > 70)}

print(passed_students)

print(student_random_score.items()) # returns all key-values as tuples
# dict_items([('Alex', 62), ('Beth', 79), ('Caroline', 72), ('Dave', 86), ('Eleanor', 67), ('Freddie', 61)])


# notice "key-value" pair is as tuple, "(nam, score)" for "name : score"

# python Dictionary_Comprehension.py