class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0


    def size(self):
        return self.stack_size


    def is_empty(self):
        if self.stack_size:
            return False
        else:
            return True


    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]


    def push(self, data):
        self.stack_list.append(data)
        self.stack_size += 1

    def pop(self):
        if not self.is_empty():
            self.stack_size -= 1
            self.stack_list.pop()
