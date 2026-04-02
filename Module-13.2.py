# 1. ЗАГОЛОВОК 
print("Задача 1. Сумма чисел 2")
print(len("Задача 1. Сумма чисел 2") * "=")
print()

# 2. ОПРЕДЕЛЕНИЕ ФУНКЦИЙ 
def get_summa_n(n):
    return sum(range(1, n + 1))

# 3. ВВОД ДАННЫХ 
number = int(input("Введите число: "))

# 4. ПЕРВЫЙ ЭТАП (Вызываем функцию первый раз)
first_result = get_summa_n(number)
print(f"Сумма от 1 до {number} = {first_result}")

# 5. ВТОРОЙ ЭТАП (Передаем результат первой функции во вторую)
second_result = get_summa_n(first_result)
print(f"Сумма от 1 до {first_result} = {second_result}")