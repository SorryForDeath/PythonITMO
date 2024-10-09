from xml.etree.ElementTree import tostring

class HashTable:
    _hash = dict()
    dimension = int()
    def __init__(self, n):
        self.dimension = n
        self.add_to_hash("Arthur Morgan")
        self.add_to_hash("LexProxima")
        self.add_to_hash("Been To Hell")

    def hashFunc(self, st):
        temp = ""
        for i in st:
            temp +=  str(ord(i))
        return int(temp) % self.dimension

    def add_to_hash(self, st):
        if self.dimension == len(self._hash) - 25:
            self.dimension += 128
        index = self.hashFunc(st)
        if index in self._hash.keys():
            if isinstance(self._hash[index], list):
                self._hash[index].append(st)
            else:
                self._hash[index] = [self._hash[index]]
                self._hash[index].append(st)
        else:
            self._hash[index] = st

    def find_str(self, st):
        index = self.hashFunc(st)
        if index in self._hash.keys():
            if isinstance(self._hash[index], list):
                if st in self._hash[index]:
                    return index
            else:
                if st == self._hash[index]:
                    return index
        return False

    def remove(self, st):
        if self.find_str(st):
            index = self.hashFunc(st)
            if isinstance(self._hash[index], list):
                self._hash[index].remove(st)
            else:
                del self._hash[index]

    def print_hash(self):
        print(self._hash)

hashTable = HashTable(256)
print("Добро пожаловать в консольное управление хэш-таблицей.\n"
      "Список команд:\n"
      "1 - Добавить строку в хэш-таблицу\n"
      "2 - Удалить строку из хэш-талицы\n"
      "3 - Найти строку в хэш-таблице\n"
      "4 - Вывести всю хэш-таблицу\n"
      "0 - Завершить\n")
while True:
    command = input("Введите команду для выполнения: ")
    match command:
        case '1':
            hashTable.add_to_hash(input("Какую строку вы хотите добавить? "))
        case '2':
            hashTable.remove(input("Какую строку вы хотите удалить? "))
        case '3':
           case3 = hashTable.find_str(input("Какую строку вы хотите найти? "))
           if case3:
               print(f"Ваша строка под индексом {case3}")
           else:
               print("Данной строки нет в хэш-таблице")
        case '4':
            hashTable.print_hash()
        case '0':
            print("Завершение программы")
            break
        case _:
            print("Неверная команда, попробуйте еще раз\n")