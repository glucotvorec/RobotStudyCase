"""
Данный скрип запрашивает у пользователя список школьных предметов и имена учеников, создавая два словаря.
Затем словари дополняются суммой баллов студента по всем предметам и суммой баллов по каждому предмету,
из этих данных вычисляется ученик с самым высоким средним баллом и средняя успеваемость по предмету.
"""
"""
Функция для получения списка предметов и их оценок.
"""
def get_subjects():
    subjects_dict = {}  # Словарь для хранения названий предметов и их оценок
    while True:
        subject = input("Введите название предмета или 'стоп', для завершения справочника: ")
        if subject == 'стоп':
            break  # Завершаем цикл, если пользователь ввел 'стоп'
        subjects_dict[subject] = 0  # Добавляем ключ в словарь с начальным значением 0
    return subjects_dict  # Возвращаем словарь с добавленными предметами

"""
Функция для получения списка студентов и их оценок.
"""
def get_students():
    students_dict = {}  # Словарь для хранения фамилий студентов и их оценок
    while True:
        student = input("Введите фамилию и имя студента через пробел или 'стоп', для завершения справочника: ")
        if student == "стоп":
            break  # Завершаем цикл, если пользователь ввел 'стоп'
        students_dict[student] = 0  # Добавляем ключ в словарь с начальным значением 0
    return students_dict  # Возвращаем словарь с добавленными студентами

school_subjects = get_subjects()  # Получаем список предметов
students_list = get_students()  # Получаем список студентов


print("Введите оценку по предмету")
for student in students_list:
    print(f"Студент {student}")
    for subject in school_subjects:
        while True:
            score = input(f"{subject}:")  # Запрашиваем оценку по предмету
            if score.isdigit() and 1  <= int(score) < 6: # Проверяем оценку на соответствие оценочной системе
                score = int(score)
                break
            else:
                print("Пятибалльная система, оценки от 1 до 5ти")
                continue
        
        students_list[student] += score  # Добавляем оценку к общему баллу студента
        school_subjects[subject] += score  # Добавляем оценку к общему баллу предмета

the_bast_student = max(students_list, key=students_list.get)  # Находим студента с наивысшим баллом

print(f"""Статистика:
Студент с лучшей успеваемостью:
{the_bast_student}: {students_list[the_bast_student]/len(school_subjects): .2f}\n""")

print("Средний балл по предмету")
for subject in school_subjects:
    print(f"{subject} {school_subjects[subject]/len(students_list): .2f}")