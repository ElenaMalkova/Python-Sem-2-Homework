# Подсчитать сумму цифр в вещественном числе.

print("Введите вещественное число: ")
number = input() # задаем число как строку

if number.__contains__("."): # проверяем, содержит ли число разделители разрядов
   number = number.replace(".", "") # убираем разделитель разрядов из числа
elif number.__contains__(","):
   number = number.replace(",", "")

sum_of_digits = 0
for i in number:
    sum_of_digits +=int(i) # преобразовываем элементы строки в целые числа и складываем их

print(f"Cумма цифр в числе: {sum_of_digits}")


