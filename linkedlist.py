import node as n

class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, new_data):
        new_node = n.Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_linked_list(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next
