# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например: positions = [1, 3, 6]).

# Method
def fill_list(x): # Метод заполнения списка значениями от -х до х
    list = []
    for i in range(-x, x+1):
        list.append(i)
    return list

# Code
n = int(input("Введите положительное целое число n: "))
print(f"Cписок из элементов, заполненных числами промежутка [-n, n]: {fill_list(n)}")

with open("positions.txt", "r") as file:   # Формирование списка индексов с использованием данных из файла
    num = file.read()
    positions = []
    positions = num.split("\n")   # Содержание файла дробится по признаку переноса на новую строку

result = 1
my_list = fill_list(n)
for i in positions:    # Произведение эл-тов из списка значений, стоящих под индексами из списка индексов 
    result *= my_list[int(i)]

print(f"Произведение элементов с индексами {positions} равно {result}")
