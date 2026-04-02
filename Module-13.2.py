# # 1. ЗАГОЛОВОК 
# print("Задача 1. Сумма чисел 2")
# print(len("Задача 1. Сумма чисел 2") * "=")
# print()

# # 2. ОПРЕДЕЛЕНИЕ ФУНКЦИЙ 
# def get_summa_n(n):
#     return sum(range(1, n + 1))

# # 3. ВВОД ДАННЫХ 
# number = int(input("Введите число: "))

# # 4. ПЕРВЫЙ ЭТАП (Вызываем функцию первый раз)
# first_result = get_summa_n(number)
# print(f"Сумма от 1 до {number} = {first_result}")

# # 5. ВТОРОЙ ЭТАП (Передаем результат первой функции во вторую)
# second_result = get_summa_n(first_result)
# print(f"Сумма от 1 до {first_result} = {second_result}")

# ЗАГОЛОВОК
print("Задача 3. Приоритет задач")
print(len("Задача 3. Приоритет задач") * "*")
print()

# Функция для подсчета количества цифр в числе
def numeral_count(number):
    # Если число отрицательное, по условию в нем 0 цифр
    if number < 0:
        return 0
    
    # Преобразуем число в строку, чтобы посчитать символы (цифры)
    number_as_str = str(number)
    return len(number_as_str)

# --- ОСНОВНАЯ ПРОГРАММА ---

# Узнаем, сколько чисел будем проверять
task_count = int(input("Введите кол-во задач: "))

# Переменные для хранения самого длинного числа
max_digits = -1  # Начинаем с -1, так как любое кол-во цифр (даже 0) будет больше
best_number = 0

for i in range(task_count):
    # Спрашиваем число у пользователя
    current_number = int(input(f"Введите {i + 1}-е число: "))
    
    # Считаем, сколько в нем цифр, используя нашу функцию
    current_digits = numeral_count(current_number)
    
    # Если текущее число длиннее, чем то, что мы видели раньше
    if current_digits > max_digits:
        max_digits = current_digits # Запоминаем новый рекорд длины
        best_number = current_number # Запоминаем само число-рекордсмен

# Выводим финальный результат
print("-" * 20) # Отделим ввод от вывода для красоты
print(f"Первое максимально длинное число: {best_number}")