""" 
Данная программа запрашивает у пользователя путь к файлу с арифметическими примерами, 
используя функцию eval() проводит вычисления. Результат заноситься в файл result.txt,
ошибки в error.txt
"""
def read_exercises_file(path_to_exercises_file):

  # Чтение файла с арифметическими примерами.
  # path_to_exercises_file: Путь к файлу с упражнениями.
  # return: Список строк с упражнениями.

    with open(path_to_exercises_file, 'r') as r_file:
        exercises_list = r_file.readlines()
    return exercises_list

def write_results_to_file(results_of_exercises):
    
  # Запись результатов упражнений в файл.
    
  # results_of_exercises: Словарь с результатами упражнений.
    
    ns = "\n"
    with open("result.txt", "w") as w_file:
        for number, result in results_of_exercises.items():
            w_file.write(f"{number} {result} {ns}")

def log_errors_to_file(exceptions):
    
  # Запись ошибок в файл.
    
  # exceptions: Словарь с ошибками.
    
    with open("error.txt", "w") as err_file:
        for number, error in exceptions.items():
            err_file.write(f"{number} {error} {ns}")

def process_exercises(exercises_list):
    
  # Обработка упражнений и запись результатов.
    
  # exercises_list: Список строк с упражнениями.
    
    exercises_result_list = {}
    exercises_error_list = {}
    string_number = 0
    for exercises in exercises_list:
        string_number += 1
        try:
            result = eval(exercises)
        except NameError as ex:
            exercises_error_list[string_number] = ex
            print(f"{string_number} {exercises_error_list[string_number]}")
        else:
            exercises_result_list[string_number] = result
            print(f"{string_number}{exercises_result_list[string_number]}")
    write_results_to_file(exercises_result_list)
    log_errors_to_file(exercises_error_list)

# Основная логика программы
path_to_exercises_file = input("Enter path to file with maths exercises: ")
exercises_list = read_exercises_file(path_to_exercises_file)
process_exercises(exercises_list)