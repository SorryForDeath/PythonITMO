import re
number = 0
def regular(pattern, text):
    cn = 0
    global number
    number += 1
    a = re.findall(pattern, text)
    print(f"\n№{number}\nКоличество совпадений регулярного выражения {pattern} в файле:")
    print(len(a))
    print('Первые 10 совпадений')
    for i in a:
        cn += 1
        print(i)
        if cn == 10:
            break
with open('Stephen_King_-_It.txt') as reader:
    text = reader.read()
    regular(r'\d{4}', text)
    regular(r'\b[A-Z][a-z]+\b', text)
    regular(r'It', text)
