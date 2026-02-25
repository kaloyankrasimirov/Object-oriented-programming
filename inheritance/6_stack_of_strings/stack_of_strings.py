class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not any(self.data)

    def __str__(self):
        return "[" + ", ".join(self.data[::-1]) + "]"
