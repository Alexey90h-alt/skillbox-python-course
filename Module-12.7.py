import math

print("Задача «Наибольший общий делитель»")
print(len("Задача «Наибольший общий делитель»") * "⁕")
print()

print("Что нужно сделать.\nНапишите функцию, вычисляющую наибольший\nобщий делитель двух чисел.")
print()

def get_gcd(a, b):
    return math.gcd(a, b)

num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

result = get_gcd(num_1, num_2)
print(f"Наибольший общий делитель: {result}")
