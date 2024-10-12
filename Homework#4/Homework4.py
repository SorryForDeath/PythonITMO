import re
import requests
import json
import random
import numpy as np
from string import printable

#Задание №1
email = r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)'
number = r'(?:\+?\d{1,2}\s?)?(?:\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{2,4}[\s.-]?\d{2,4}'
try:
    with open('Email.txt') as f:
        r = f.read()
        emails = re.findall(email, r)
        numbers = [match.group() for match in re.finditer(number, r)]
except Exception as ex:
    print(f"Ошибка: {ex}")
try:
    with open('final_answer.txt', 'w') as g:
        g.write("Список встреченных email адресов: ")
        g.write(" ".join(emails))
        g.write("\nCписок встреченных номеров: ")
        g.write(" ".join(numbers))
except Exception as ex:
    print(f"Ошибка: {ex}")
try:
    with open("final_answer.txt") as g:
        print(f"Задание №1\nДанные в финальном файле:\n{g.read()}\n")
except Exception as ex:
    print(f"Ошибка: {ex}")

#Задание №2
response = requests.get('https://api.github.com/users/SorryForDeath')
contents = response.text
data = json.loads(contents)
print(f'Задание №2\nЛогин пользователя: {data['login']}'
      f'\nИмя пользователя: {data['name']}'
      f'\nКоличество репозиториев: {data['public_repos']}')

#Задание №3
arr = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
for i in range(10):
    for j in range(10):
        arr[i][j] = round(random.uniform(-5, 5))

print(f'\nЗадание№3\nСлучайная матрица:\n{('\n'.join('\t'.join(map(str, row)) for row in arr))}')
print(f"Определитель матрицы: {round(np.linalg.det(arr))}")
if np.linalg.det(arr) == 0:
    print("Невозможно транспонировать вырожденную матрицу, далее будет произведена работа с изначальной матрицей")
    print(f"Ранг матрицы: {np.linalg.matrix_rank(arr)}")
    print(f"Собственные значения и векторы (чтобы это ни было):\n {np.linalg.eig(arr)}")
    arr2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(10):
        for j in range(10):
            arr2[i][j] = round(random.uniform(-5, 5))
    print(f'Вторая матрица:\n{('\n'.join('\t'.join(map(str, row)) for row in arr2))}')
    print(f'Первая матрица:\n{('\n'.join('\t'.join(map(str, row)) for row in arr))}')
    print(f"Сумма двух матриц:\n{np.add(arr, arr2)}")
    print(f"Произведение двух матриц:\n{np.dot(arr, arr2)}")
else:
    trans = np.transpose(arr)
    print(f'\nТранспонированная матрица:\n{trans}')
    print(f"Ранг матрицы: {np.linalg.matrix_rank(trans)}")
    print(f"Собственные значения и векторы (чтобы это ни было):\n {np.linalg.eig(trans)}")
    arr2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(10):
        for j in range(10):
            arr2[i][j] = round(random.uniform(-5, 5))
    print(f'Вторая матрица:\n{('\n'.join('\t'.join(map(str, row)) for row in arr2))}')
    print(f'Первая матрица:\n{('\n'.join('\t'.join(map(str, row)) for row in trans))}')
    print(f"Сумма двух матриц:\n{np.add(trans, arr2)}")
    print(f"Произведение двух матриц:\n{np.dot(trans, arr2)}")

#Задание №4
try:
    size_of_password = int(input("\nЗадание №4\nДлина пароля: "))
    password = ""
    for i in range(size_of_password):
        password += random.choice(
            list(printable))  # Я решил, что специальные символы есть всевозможные символы, в том числе и пробел и символ новой строки
    print(f"Your password: {password}")
except Exception as ex:
    print(f'Возникла ошибка {ex}. Пароль будет сгенерирован стандартной длины - 10 символов')
    password = ''
    for i in range(10):
        password += random.choice(
            list(printable))
    print(f"Your password: {password}")

