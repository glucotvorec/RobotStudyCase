def get_subjects():
    subjects_dict = {}
    while True:
        subject = input("Введите название предмета или 'стоп',  для завершения справочника: ")
        if subject == 'стоп':
            break
        subjects_dict[subject] = 0
    return subjects_dict

def get_students():
    students_dict = {}
    while True:
        student = input("Введите фамилию и имя студента через пробел или стоп, для завершения справочника: ")
        if student == "стоп":
            break
        students_dict[student] = 0
    return students_dict
school_subjects = get_subjects()
students_list = get_students()
#average_score_subjects = {}
average_students_score = {}
print("Введите оценку по предмету")
for student in students_list:
    average_students_score[student] = 0
    print(f"Студент {student}")
    for subject in school_subjects:
        score = int(input(f"{subject}:"))
        students_list[student] += score
        school_subjects[subject] += score

the_bast_student = max(students_list, key=students_list.get)

print(f"""Статистика:
Студент с лучшей успеваемостью:
{the_bast_student}: {students_list[the_bast_student]/len(school_subjects): .2f}""")
      
print("Средний балл по предмету")
for subject in school_subjects:
    print(f"{subject} {school_subjects[subject]/len(students_list)}")