
"""Данная программа анализирует файл и выдаёт статистику по каждому встречающемуся символу за исключение пробела
а так же 10 строк из текста где встречается имя Андрей"""

ns = "\n"  # Новая строка
counter = 0  # Счетчик символов
string_counter = 0  # Счетчик строк с упоминанием "Андре"
string_list = []  # Список всех строк текста
ten_string = []  # Список из 10 строк с упоминанием "Андре"
alphabet = {}  # Словарь для подсчета частоты символов

# Открываем файл для чтения, используя кодировку cp1251
with open("/home/swordsman/temp/war_and_peace.txt", 'r', encoding='cp1251') as text_file:
    # Читаем содержимое файла и разбиваем его на строки
    content = text_file.read()
    string_list = content.split('.')

    # Проходимся по каждой строке и каждому символу в ней
    for line in content:
        for symbol in line:
            # Пропускаем пробелы и табы
            if symbol == " " or symbol == "\t":
                continue
            # Проверяем, является ли символ буквой и добавляем его в словарь, если еще не добавлен
            elif symbol.isalpha() and not alphabet.get(symbol.lower()):
                alphabet[symbol.lower()] = 1
                counter += 1
            # Увеличиваем счетчик для уже существующего символа
            elif symbol.isalpha() and alphabet.get(symbol.lower()):
                alphabet[symbol.lower()] += 1
                counter += 1
            # Добавляем новый символ в словарь, если его там нет
            elif not alphabet.get(symbol):
                alphabet[symbol] = 1
                counter += 1
            # Увеличиваем счетчик для уже существующего символа
            else:
                alphabet[symbol] += 1
                counter += 1

    # Проходимся по списку строк и собираем строки с упоминанием "Андре"
    ten_string = [sentence for sentence in string_list if "Андре" in sentence][:10]
# Сортируем словарь символов по алфавиту
alphabet = dict(sorted(alphabet.items()))

# Выводим результаты: частоту каждого символа и строки с упоминанием "Андре"
print("Статистика:")
for letter, number in alphabet.items():
    print(f"{letter}: {number/counter: .5f}{ns}")
print("Предложения с именем Андрей:")
for sentence in ten_string:
    print(f"{sentence.strip()}")