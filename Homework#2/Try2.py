import numpy as np
import re

#Для 1 задания
def joinList(l1, l2):
    final_list = []
    for i in range(len(list1)):
        final_list.append(list1[i])
        final_list.append(list2[i])
    return final_list
#Для 2 задания
def sortAge(dic):
    return sorted([i for i in dic if i[1] >= 18], key=lambda x: x[1])


#Для 3 задания
def minor(matrix, k):
    res = []
    for i in matrix[1:]:
        row = []
        for j in range(len(i)):
            if j != k:
                row.append(i[j])
        res.append(row)
    return res
def matrixDet(matrix):
    n = len(matrix)
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    s = 0
    z = 1
    for i in range(n):
        s = s + z * matrix[0][i] * matrixDet(minor(matrix, i))
        z = -z
    return s

#Для 4 задания
def swapKeyValue(dic):
    tempDic = dict()
    for i in dic:
        tempDic[dic[i]] = i
    return tempDic


#Для 5 задания
def listCross(l):
    tempSet = l[0]
    for i in l:
        tempSet = tempSet & i
    return tempSet

#Задание 6
def strWork(st):
    newStr = st.lower()
    newStr = re.sub(r'[^\w\s]', '', newStr)
    newStr = newStr.split(" ")
    dic = dict()
    for i in newStr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return sorted(dic.items(), key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    #Задание №1
    list1 = [1,2,3]
    list2 = ['a', 'b', 'c']
    print(f'Задание№1\nСоединенный список: {joinList(list1, list2)}\n')

    #Задание №2
    list1 = [('Mike', 12), ('Angela', 39), ('Chester', 20), ('Alexey', 10), ('Katya', 18), ('Masha', 25)]
    print(f'Задание№2\nОтсортированный список, где всем участникам >= 18 лет {sortAge(list1)}\n')

    #Задание 3
    matrix = [
        [3, 2, 1, 4, 2, 1, 5, 2, 3, 4],
        [1, 4, 2, 3, 5, 1, 2, 4, 1, 3],
        [2, 1, 3, 5, 4, 2, 1, 3, 2, 1],
        [4, 3, 1, 2, 1, 5, 4, 3, 2, 1],
        [2, 5, 4, 1, 3, 2, 1, 5, 4, 2],
        [1, 2, 3, 4, 5, 3, 1, 2, 3, 1],
        [5, 1, 2, 3, 4, 1, 5, 2, 3, 4],
        [2, 4, 3, 1, 2, 5, 3, 1, 4, 2],
        [3, 1, 2, 5, 1, 3, 2, 4, 5, 3],
        [4, 3, 1, 2, 4, 1, 5, 3, 2, 1]
    ]
    #Определитель считается через миноры первого столбца. Способ неэффектиный, очень долгий, на матрице 20 на 20 считается больше часа,тем не менее способ рабочий.
    print(f'Заадание№3.\nОпределитель матрицы:\n{('\n'.join('\t'.join(map(str, row)) for row in matrix))} = {matrixDet(matrix)}')
    print(f'Проверка результата через библиотечный метод: {round(np.linalg.det(matrix), 3)}')

    #Задание 4
    dic = {'a': 1, 'b': 2, 'c': 3}
    print(f"Задание №4\nРезультат смены местами ключа и значения {dic} = {swapKeyValue(dic)}")

    #Задание 5
    l1 = [{1, 2, 3, 4}, {2, 3, 4}, {3, 4, 5}]
    print(f"Задание №5\nРезультат пересечения множеств {l1} = {listCross(l1)}")

    # Задание 6
    s = "Мистер и миссис Дурсль проживали в доме номер четыре по Тисовой улице и всегда с гордостью заявляли, что они, слава богу, абсолютно нормальные люди. Уж от кого-кого, а от них никак нельзя было ожидать, чтобы они попали в какую-нибудь странную или загадочную ситуацию. Мистер и миссис Дурсль весьма неодобрительно относились к любым странностям, загадкам и прочей ерунде."
    print(f"Задание №6\nФинальный словарь:\n{strWork(s)}")
