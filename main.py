class DoubleLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = self.Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = self.Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        if index <= 0:
            self.prepend(value)
        elif self.length > 0 and index < self.length:
            new_node = self.Node(value)
            prev_el = self.head
            for _ in range(index - 1):
                prev_el = prev_el.next
            new_node.next = prev_el.next
            prev_el.next.prev = new_node
            prev_el.next = new_node
            new_node.prev = prev_el
            self.length += 1
        else:
            self.append(value)

    def delete(self, value):
        if not self.length:
            return None
        elif self.head.value == value:
            self.head.next.prev = None
            self.head = self.head.next
        else:
            current = self.head
            while current and value != current.value:
                current = current.next
            if not current:
                return None
            elif current is self.tail:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
        self.length -= 1

    def find(self, value):
        index = 0
        current = self.head
        while index < self.length:
            if value == current.value:
                return index
            current = current.next
            index += 1
        return -1

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


if __name__ == '__main__':
    a = DoubleLinkedList()
    b = DoubleLinkedList()
#  Добавление в начало:
    a.append(4)
    a.append(6)
    print(list(a), 'метод append()')
#  Добавление в конец:
    a.prepend(3)
    a.prepend(1)
    print(list(a), 'метод prepend()')
#  Вставка по индексу:
    a.insert(2, 25)
    a.insert(0, 0)
    a.insert(100, 50)
    a.insert(-1, -2)
    print(list(a), 'метод insert()')
#  Удаление по значению:
    b.delete(6)
    print(list(b), 'метод delete() пустой список')

    a.delete(25)
    a.delete(0)
    a.delete(51)
    a.delete(50)
    print(list(a), 'метод delete()')

#  Возвращение индекса элемента по значению:
    print(a.find(6), 'метод find()')
    print(a.find(-10), 'метод find()')
    print(b.find(1), 'метод find() пустой список')
#  Длина списка:
    print(f'Количестов элементов {len(a)}')
