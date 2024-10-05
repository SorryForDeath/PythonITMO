from functools import reduce
import re

def is_prime(pr):
    if pr == 0 or pr == 1 or pr < 0:
        return -1
    if pr % 2 == 0:
        return False
    for i in range(3, round(pr / 2), 2):
        if pr % i == 0:
            return False
    return True


def own_map(some_list, func):
    return [func(i) for i in some_list]

def str_things():
    answer = {
        "lines": 0,
        "words": 0,
        "symbols": 0
    }
    mx = ''
    with open("zombie.txt") as g:
        for line in g:
            answer["lines"] += 1
            ls = line.split(" ")
            answer["words"] += len(ls)
            for i in ls:
                i = re.sub(r'[,.!?]', '', i)
                if len(i) > len(mx):
                    mx = i
            les = ''.join(ls)
            answer["symbols"] += len(les)
    return answer, mx


if __name__ == "__main__":
    #Задание №1
    a = [1, 2, 3, 5, 7, 9, 11, 20]
    print(f'Задание №1\nОригинальный список: {a}')
    _map = list(map(lambda x: x**3, a))
    print(f'Список, состоящий из кубов первого: {_map}')
    _filter = list(filter(lambda x: x % 2 == 0, a))
    print(f'Только четные элементы списка: {_filter}')
    _reduce = reduce(lambda x, y: x * y, _filter)
    print(f'Результат применения reduce: {_reduce}')

    #Задание №2
    print("Задание №2\n")
    prime = int(input("Введите число для проверки на простоту "))
    if is_prime(prime) == -1:
        print ("Числа 0 и 1 не являются сложными или простыми, а для отрицательных проверка на простоту не актуальна")
    else:
        if is_prime(prime):
            print(f'Число {prime} простое')
        else:
            print(f'Число {prime} сложное')

    #Задание №3
    print("Задание №3\nИсходный список: ")
    a = [11, 3, 5, 4]
    print(a)
    print(f"Результат работы own_map (Проверяет каждое число списка на простоту): {own_map(a, lambda x: is_prime(x))}")

    #Задание №4
    print(f'Задание №4:\n{str_things()[0]}\nСамое длинное слово: {str_things()[1]}, его длина: {len(str_things()[1])}')


