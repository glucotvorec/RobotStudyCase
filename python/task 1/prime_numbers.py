"""Программа получает от пользователя максимальное число в ряду, и используя адоптированный алгоритм "решето Эратосфена" 
убирает все составные числа из ряда. """
def sieve_of_eratosthenes(limit):
    # Создаем список, заполненный True, что представляет все числа до limit
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 и 1 не являются простыми числами

    # Перебираем числа и исключаем те, которые не являются простыми
    for current in range(2, int(limit**0.5) + 1): # Проходим последовательность чисел квадрат которых входит в диапазон ограниченный limit
        if sieve[current]:
            for multiple in range(current * current, limit + 1, current): # Перебор последовательности на основе n**2, n**2+n, n**2+2n.
                sieve[multiple] = False # Помечаем составные числа

    # Возвращаем список простых чисел
    prime_numbers = [i for i in range(2, limit + 1) if sieve[i]] # "Просеиваем" последовательность используя список sieve
    return prime_numbers

# Ввод данных от пользователя
while True:
#Используем цикл для проверки данных вводимых пользователем
    max_limit = input("Введите максимальное число: ")
    try:
        #Если введено не число или число меньше 2, выдаём ошибку и ждём повторный ввод
        if not max_limit.isdigit() or int(max_limit) < 2:
            raise ValueError()
    except (ValueError):
        print("Введите число больше 2")
    else:
        max_limit = int(max_limit)
        break
prime_numbers = sieve_of_eratosthenes(max_limit)
print(prime_numbers)