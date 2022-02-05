from double_linkedlist import DoubleLinkedList

class MyQueue:
    def __init__(self):
        self.items = DoubleLinkedList()

    def is_empty(self):
        return self.items.length == 0

    def front(self):
        if self.is_empty():
            return None
        else:
            return self.items.head.data

    def rear(self):
        if self.is_empty():
            return None
        else:
            return self.items.tail.data

    def size(self):
        return self.items.length

    def enqueue(self, data):
        return self.items.insert_tail(data)

    def dequeue(self):
        return self.items.remove_head()

    def print_list(self):
        return self.items.__str__()