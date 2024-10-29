def wordToInt(word)->int:
    summ = 0
    for i in word:
        summ += ord(i)
    return summ

words = 'tree, mountain, river, cloud, book, chair, light, window, phone, mirror, sky, dream, road, smile, shadow'
a = words.split(', ')
dictForBinary = dict()
for i in a:
    dictForBinary[i] = wordToInt(i)
sortedForBinary = dict(sorted(dictForBinary.items(), key=lambda x: x[1]))
print(f'Отсортированный словарь:\n{sortedForBinary}')
value = input("Какое слово ищем?\n")
value = re.sub(r' ', '', value)
low = 0
high = len(a) - 1
mid = len(a) // 2


while list(sortedForBinary.keys())[mid] != value and low <= high:
    if wordToInt(value) > list(sortedForBinary.values())[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print('Такого слова нет в словаре')
else:
    print('ID =', mid)
