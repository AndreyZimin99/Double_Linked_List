from typing import Any, Generator


class DoubleLinkedList:
    class Node:
        def __init__(self, value: Any):
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def append(self, value: Any):
        new_node = self.Node(value)
        if self._length == 0:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._length += 1

    def prepend(self, value: Any):
        new_node = self.Node(value)
        if self._length == 0:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._length += 1

    def insert(self, index: int, value: Any):
        if index <= 0:
            self.prepend(value)
        elif self._length > 0 and index < self._length:
            new_node = self.Node(value)
            prev_el = self._head
            for _ in range(index - 1):
                prev_el = prev_el.next
            new_node.next = prev_el.next
            prev_el.next.prev = new_node
            prev_el.next = new_node
            new_node.prev = prev_el
            self._length += 1
        else:
            self.append(value)

    def delete(self, value: Any):
        if not self._length:
            return None
        elif self._head.value == value:
            if self._length == 1:
                self._head = None
            else:
                self._head.next.prev = None
                self._head = self._head.next
        else:
            current = self._head
            while current and value != current.value:
                current = current.next
            if not current:
                return None
            elif current is self._tail:
                self._tail.prev.next = None
                self._tail = self._tail.prev
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
        self._length -= 1

    def find(self, value: Any) -> int:
        index = 0
        current = self._head
        while index < self._length:
            if value == current.value:
                return index
            current = current.next
            index += 1
        return -1

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Generator[Any, None, None]:
        current = self._head
        while current:
            yield current.value
            current = current.next


if __name__ == '__main__':
    a = DoubleLinkedList()
    b = DoubleLinkedList()
    d = DoubleLinkedList()
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
#  Удаление из списка содержащего 1 элемент:
    d.append(1)
    d.delete(15)
    print(list(d))
    d.delete(1)
    print(list(d), 'delete() для списка с 1 элементом')
