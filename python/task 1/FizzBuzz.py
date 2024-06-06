"""
Игра Fizz Buzz.
Запрашивает у игрока число которым должен завершаться ряд
и выполняет проверку чисел в последовательности на возможность деления на 3 и 5.
При делении на 3 выводиться слово "Fizz", на 5 "Buzz". Если на 3 и 5, то "Fizz Buzz" 
"""
while True:
#Используем цикл для проверки данных вводимых игроком
    user_set_number = input("Enter the max number: ")
    try:
        #Если введено не число или число меньше 0, выдаём ошибку и ждём повторный ввод
        if not user_set_number.isdigit() or int(user_set_number) < 1:
            raise ValueError()
    except (ValueError):
        print("Specify an integer greater than 0")
    else:
        break
#Генерируем последовательность чисел от нуля до user_set_number
for number in range(1,int(user_set_number) + 1):
    if int(number) % 3 == 0 and int(number) % 5 == 0:
        print("Fizz Buzz")
    elif int(number) % 3 == 0:
        print("Fizz")
    elif int(number) % 5 == 0:
        print("Buzz")
    else:
        print(number)