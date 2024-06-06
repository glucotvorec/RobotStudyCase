
"""
Программа запрашивает 3 стороны треугольника, используя "неравенство треугольника" проводит
проверку его существования, и далее вычисляет его углы, периметр и площадь.
"""
import math

def is_triangle(a, b, c):
    #Проверяем, могут ли стороны a, b и c образовать треугольник.
    return a + b > c and a + c > b and b + c > a

def triangle_angles(a, b, c):
    #Вычисляем углы треугольника по его сторонам.
    angle_a = round(math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c))), 2)
    angle_b = round(math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c))), 2)
    angle_c = round(math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b))), 2)
    return angle_a, angle_b, angle_c
def triangle_area(a, b, c):
    #Вычисляем площадь треугольника по формуле Герона.
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def triangle_perimeter(a, b, c):
    #Вычисляем периметр треугольника.
    return a + b + c

# Ввод данных от пользователя
while True:
#Используем цикл для проверки данных вводимых пользователем
    a = input("Введите длину стороны a: ")
    b = input("Введите длину стороны b: ")
    c = input("Введите длину стороны c: ")
    try:
        #Если введено не число или число меньше 0, выдаём ошибку и ждём повторный ввод
        if not a.isdigit() or float(a) < 0:
            raise ValueError()
        elif not b.isdigit() or float(b) < 0:
            raise ValueError()
        elif not c.isdigit() or float(c) < 0:
            raise ValueError()
    except (ValueError):
        print("Введите число больше 0")
    else:
        a = float(a)
        b = float(b)
        c = float(c)
        break

# Проверка возможности существования треугольника
if not is_triangle(a, b, c):
    print("Такой треугольник невозможен.")
else:
    # Вычисление углов, площади и периметра
    angles = triangle_angles(a, b, c)
    area = triangle_area(a, b, c)
    perimeter = triangle_perimeter(a, b, c)
    
    print(f"Углы треугольника: {angles}")
    print(f"Площадь треугольника: {area}")
    print(f"Периметр треугольника: {perimeter}")