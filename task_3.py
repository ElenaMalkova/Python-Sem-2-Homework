# Задать список из n чисел последовательности  (1 + 1/n)**n и вывести на экран их сумму.

n = int(input("Введите натуральное число n "))
result = []
value = 1.0
sum = float()

for i in range(1, n+1):  # В range лежат порядковые номера чисел от 1 до n
    value = round((1 + 1/i)**i, 2)
    result.append(value) # В пустой список добавляем значение числа, выведенное по формуле 
    sum += value

print(*result, sep=", ") 
print(f"Сумма чисел в последовательности равна {sum}")

