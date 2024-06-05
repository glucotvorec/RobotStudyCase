
def generate_fibonacci_sequence(max_value):
    """
    Генерирует последовательность чисел Фибоначчи до указанного максимального значения.
    
    :param max_value: Максимальное значение чисел Фибоначчи, которое нужно сгенерировать.
    :return: Список чисел Фибоначчи до max_value-го числа Фибоначчи.
    """
    sequence = [0, 1]
    if max_value <= 1:
        # Если max_value меньше или равно 1, возвращаем пустой список
        return []
    else:
        for i in range(2, max_value):
            # Добавляем следующее число Фибоначчи к списку
            sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

fibonacci_sequence = generate_fibonacci_sequence(10)
# Проверяем, что длина списка соответствует ожидаемому значению
assert len(fibonacci_sequence) == 10
print(f"{fibonacci_sequence}")