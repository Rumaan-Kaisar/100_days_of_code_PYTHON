# key - value pair

studentScore = {
    "Harry": 81, 
    "Ron": 72, 
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grade = {}

for student in studentScore:
  if 91 <= studentScore[student] < 100:
    grade = "Outstanding"
  elif 81 <= studentScore[student] <= 90:
    grade = "Exceed Expectations"
  elif 70 <= studentScore[student] <= 80:
    grade = "Acceptable"
  elif studentScore[student] < 70:
    grade = "Failed"
  
  student_grade[student] = grade


print(student_grade)


# python grade.py