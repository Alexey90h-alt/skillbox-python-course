import math

print("(●'◡'●)Задача 1. Герон")
print(len("(●'◡'●)Задача 1. Герон") * "⁕")
print()

def get_side(label):
    while True:
        try:
            value = float(input(f"Введите значение стороны {label}: "))
            if value <= 0:
                print("Ошибка: Сторона должна быть больше нуля!")
                continue
            return value
        except ValueError:
            print("Ошибка, введите число.")

# a,b,c - длины сторон треугольника ▲
a = get_side("A")
b = get_side("B")
c = get_side("C")

if a + b > c and a + c > b and b + c > a:

    # p - полупериметр треугольника △
    p = (a + b + c) / 2

    # 👌Решение S= √ (p * (p - a)*(p - b)*(p - c))
    square = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Площадь треугольника = {round(square, 2)}")
else:
    print("Это не треугольник.")