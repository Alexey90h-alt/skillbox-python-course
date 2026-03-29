# import math

# print("(●'◡'●)Задача 1. Герон")
# print(len("(●'◡'●)Задача 1. Герон") * "⁕")
# print()

# def get_side(label):
#     while True:
#         try:
#             value = float(input(f"Введите значение стороны {label}: "))
#             if value <= 0:
#                 print("Ошибка: Сторона должна быть больше нуля!")
#                 continue
#             return value
#         except ValueError:
#             print("Ошибка, введите число.")

# # a,b,c - длины сторон треугольника ▲
# a = get_side("A")
# b = get_side("B")
# c = get_side("C")

# if a + b > c and a + c > b and b + c > a:

#     # p - полупериметр треугольника △
#     p = (a + b + c) / 2

#     # 👌Решение S= √ (p * (p - a)*(p - b)*(p - c))
#     square = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     print(f"Площадь треугольника = {round(square, 2)}")
# else:
#     print("Это не треугольник.")

import math

print("Система навигации игрока")
print(len("Система навигации игрока") * "-")
print()

# 1. Получаем данные от игрока (используем float, так как расстояние может быть вещественным числом)
distance = float(input("Введите пройденное расстояние: "))
angle_degree = float(input("Введите угол движения (в градусах): "))

# Нужно перевести градусы в радианы с помощью math.radians
angle_rad = math.radians(angle_degree)

# 2. Считаем смещение по осям
# x = расстояние * cos(угла)
# y = расстояние * sin(угла)
new_x = distance * math.cos(angle_rad)
new_y = distance * math.sin(angle_rad)

# 3. Выводим результат (округлим до 2 знаков для красоты)
print(f"\nНовые координаты персонажа:")
print(f"По горизонтали (X): {round(new_x, 2)}")
print(f"По вертикали (Y): {round(new_y, 2)}")
print(f"Итоговая точка: ({round(new_x, 2)}, {round(new_y, 2)})")