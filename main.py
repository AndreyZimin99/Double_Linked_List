class DoubleLinkedList:
    class Node:
        def __init__(self, value=0, next=None, prev=None):
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.length = length

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
        if self.length > 0 and index < self.length:
            new_node = self.Node(value)
            self.length += 1
            pass
        else:
            self.append(value)

    def cheсk_empty_list():
        pass


# a.append(5)
