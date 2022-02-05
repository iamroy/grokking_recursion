from node import Node2

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_head(self):
        if self.head is not None:
            return self.head
        else:
            return None

    def is_empty(self):
        if self.head is not None:
            return False
        else:
            return True

    def insert_tail(self, element):
        new_node = Node2(element)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

        self.length += 1
        return


    def remove_head(self):
        if self.is_empty():
            return None

        head_node = self.get_head()

        if self.length == 1:
            self.head = None
            self.tain = None
        else:

            self.head = head_node.next
            self.head.previous = None
            head_node.next = None

        self.length -= 1

        return head_node.data


    def tail_node(self):
        if not self.is_empty():
            return self.tail
        else:
            return False

    def __str__(self):
        val = ""
        if (self.is_empty()):
            return ""
        temp = self.head
        val = "[" + str(temp.data) + ", "
        temp = temp.next

        while (temp.next):
            val = val + str(temp.data) + ", "
            temp = temp.next
        val = val + str(temp.data) + "]"
        return val