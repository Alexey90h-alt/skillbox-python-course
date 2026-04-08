# print("Задача 2. Очень простая задача")

# '''У вас есть список numbers. 
# Напишите программу, которая заполняет список 
# числами от 0 до 100 и выводит его на экран.'''

# length = len("Задача 2. Очень простая задача") * "*"
# print(length)
# print()

# numbers = []
# for _ in range(0, 100 + 1):
#     numbers.append(_)

# print(numbers)


print("Задача 3. Контроль")
print(len("Задача 3. Контроль") * "+")
print()

# 1. Запрашиваем количество сотрудников
count = int(input("Кол-во сотрудников в офисе: "))
id_list = []

# 2. Собираем ID в список
for _ in range(count):
    new_id = int(input("ID сотрудника: "))
    id_list.append(new_id)

# 3. Запрашиваем ID для поиска
search_id = int(input("Какой ID ищем? "))

# 4. Проверяем наличие
if search_id in id_list:
    print("Сотрудник на месте")
else:
    print("Сотрудник не работает!")