# def hi_there():
#     name = input("What is your name? D-bag... ")
#     print(f"Hi there, {name}.")

# hi_there()


class Stack:
    """docstring for Stack, stack structure implementation
    practice"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)    


s = Stack()
print(s.is_empty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
