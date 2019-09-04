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
print(s.is_empty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())


def merge_ranges(meetings):
    
    merged_times = []
    meetings.sort()
    merged_times.append(meetings[0])
    for meeting in meetings[1:]:
        last_merge = merged_times.pop()
        last_start = last_merge[0]
        last_end = last_merge[1]
        current_start = meeting[0]
        current_end = meeting[1]
        if current_start > last_start and current_start <= last_end:
            if current_end > last_end:
                merged_times.append((last_start, current_end))
            else:
                merged_times.append(last_merge)
        else:
            merged_times.append(last_merge)
            merged_times.append(meeting)
    return merged_times