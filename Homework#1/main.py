from datetime import datetime as dt
#Задание 1
print("Задание №1\nВведите два числа")
x = int(input())
y = int(input())
print(f'Сумма: {x + y}\nРазность: {x - y}\nПроизведение: {x * y}')
print(f'Деление x на y: {x / y}\nОстаток от деления x на y: {x % y}\nx в степени y: {x ** y}\n')

#Задание 2
print("\nЗадание №2\nВведите строку:")
x = input()
print("Каждая вторая буква строки: " + x[1::2])
print(f'Строка наоборот: {x[::-1]}')

#Задание 3
print("\nЗадание №3\nВведите список чисел. Чтобы закончить последовательность, введите -1:")
lst = [int(x) for x in iter(input, "-1")]
print(f'Длина списка: {len(lst)}\nСумма списка: {sum(lst)}')
summ = 0
for i in lst:
    summ += i
print(f'Сумма вторым способом: {summ}')
even = [i for i in lst if i % 2 == 0]
print(f'Только четные элементы списка:', end = " ")
for i in even:
    print(i, end = " ")

#Задание 4
print("\n\nЗадание 4")
lst = [x for x in range(60) if x % 2 != 0]
print("Создали спиоск нечетных от 1 до 60")
print("Числа, делящиеся на 3, на 5, но не на 15 из данного списка: ", end="")
for i in lst:
    if (i % 3 == 0) and (i % 5 == 0) and (i % 15 != 0):
        print(i, end = " ")
print(f'\nПоследний элемент из списка: {lst[-1]}')

#Задание 5
print("\nЗадание 5\nВведите 3 переменных - день, месяц и год вашего рождения")
day = int(input())
month = int(input())
year = int(input())
if month < 4:
    print("Вы родились в I квартал")
elif month < 7:
    print("Вы родились в II квартал")
elif month < 10:
    print("Вы родились в III квартал")
else: print("Вы родились в IV квартал")

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Ваш год рождения високосный")
else: print("Ваш год рождения не високосный")
print(f"С вашего рождения прошло "
      f"{(dt.now().year - year) * 365.25 + (dt.now().month - month) * 30.5 + (dt.now().day - day)}"
      f" дней")

