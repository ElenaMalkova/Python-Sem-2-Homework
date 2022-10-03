# Реализовать алгоритм перемешивания списка.

# Method

def fill_list(x): # Метод заполнения списка значениями от -х до х
    list = []
    for i in range(-x, x+1):
        list.append(i)
    return list

# Code
n = int(input("Введите положительное целое число n: "))
print(f"Cписок из элементов, заполненных числами промежутка [-n, n]: {fill_list(n)}")
my_list = fill_list(n)
list_1 = []
list_2 = []
list_3 = []

for i in my_list:
    if i%2 ==0:
        list_1.append(i)
    elif i%3 == 0:
        list_2.append(i)
    else:
        list_3.append(i)

mixed_list = list_2 + list_3 + list_1
print(f"Список после перемешивания: {mixed_list}")

# Еще один способ, для списков из любых элементов:

import random

entry_list = ["кошка", "собака", "ложка", "город", "город"]
print(f"{entry_list}")


# Функция перемешивания


def randomise_list(my_list):
    last_index = len(my_list) - 1  # Переменная для крайнего индекса
    my_new_list = []  # Создаём новый пустой список
    while last_index >= 0:  # Цикл, где от последнего индекса идём к нулю
        rnd = random.randint(0, last_index)  # Генерируем рандомное число в диапазоне индексов
        my_new_list.append(my_list[rnd])  # В пустой список добавляем элемент с рандомным индексом из данного списка
        my_list.pop(rnd)  # Из основного списка удаляем элемент, который добавили в новый список
        last_index -= 1
    return my_new_list


# Вызов функции
print(f"{randomise_list(entry_list)}")
