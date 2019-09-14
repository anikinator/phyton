from random import randint
from statistics import mean

students_list = [
    'Pupkin',
    'Telefonov',
    'Yablokov',
    'Stulov',
    'Stolov',
    'Telefonov',
    'Notebukov'
]

def generate_marks():
    return [ randint(1,5) for x in range(len(students_list))]

students_marks = {}
for i in students_list:
    students_marks[i] = generate_marks()

print(students_marks)

tmp_dict = {}
for key,value in students_marks.items():
    tmp_dict[key] = round(mean(value),2)

print(tmp_dict)
