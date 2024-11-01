from multipledispatch import dispatch

class Node:
    left = None
    right = None
    def __init__(self, value, parent):
        self.parent = parent
        self.value = value

    def hasRightChild(self):
        return self.right

    def hasLeftChild(self):
        return self.left

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def _add(self, value, current):
        if value < current.value:
            if current.hasLeftChild():
                self._add(value, current.left)
            else:
                current.left = Node(value, current)
        else:
            if current.hasRightChild():
                self._add(value, current.right)
            else:
                current.right = Node(value, current)

    def add(self, value):
        if self.root is None:
            self.root = Node(value, None)
        else:
            self._add(value, self.root)
        self.size += 1

    def preorderPrint(self, node):
        if node is None:
            return
        self.preorderPrint(node.left)
        self.preorderPrint(node.right)

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False
        if value == node.value:
            return node, parent, True
        if value < node.value:
            if node.left:
                return self.__find(node.left, node, value)
        if value > node.value:
            if node.right:
                return self.__find(node.right, node, value)
        return node
    def inorderPrint(self, node):
        if node is None:
            return
        self.inorderPrint(node.left)
        print(node.value, end=' ')
        self.inorderPrint(node.right)

    def postorderPrint(self, node):
        if node is None:
            return
        self.postorderPrint(node.left)
        self.postorderPrint(node.right)
        print(node.value, end=' ')

    def find(self, value):
        if self.root:
            result = self._get(value, self.root)
            if result:
                return result
            else:
                return None
        else:
            return None

    def _get(self, value, current):
        if current is None:
            return None
        elif current.value == value:
            return current
        elif value < current.value:
            return self._get(value, current.left)
        else:
            return self._get(value, current.right)


    def _find_min(self, node):
        if node.left:
            return self._find_min(node.left)
        return node

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            print("Такого значения нет в дереве (может быть, дерево пустое)")
            return node
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left

            else:
                min_larger_node = self._find_min(node.right)
                node.value = min_larger_node.value
                node.right = self._delete(node.right, min_larger_node.value)
        return node

    def print_tree(self):
        if self.root is None:
            print("Дерево пустое")
            return
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        if node.right is None and node.left is None:
            line = f'{node.value}'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = f'{node.value}'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = f'{node.value}'
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = f'{node.value}'
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    def inOrder(self):
        if self.root is None:
            return None
        stack = []
        current = self.root
        result = []

        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.value)
            current = current.right

        return result

    def __str__(self):
        return self.inOrder()
    def __repr__(self):
        return str(self.inOrder())

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
            if isinstance(self._hash[index], Tree):
                self._hash[index].add(st)
            else:
                self._hash[index] = Tree()
                self._hash[index].add(st)
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
        if self.dimension == len(self._hash) - 128 - 25:
            self.dimension -= 128
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