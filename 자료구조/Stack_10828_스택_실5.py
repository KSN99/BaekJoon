class Stack():
    def __init__(self):
        self.items = []
        self.top = -1

    def push(self, item):
        self.items.append(item)
        self.top += 1

    def pop(self):
        if self.is_empty() == 1:
            print(-1)
        else:
            self.items.pop()
            print(self.items[::-1])
            self.top -= 1

    def size(self):
        return len(self.items)

    def is_empty(self):
        if self.top == -1:
            return 1
        else: return 0
    def peek(self):
        if self.is_empty() == 1:
            print(-1)
        else:
            print(self.items[self.top])

stack = Stack()
X = int(input())
for i in range(X):
    stack_cmd = input()
    cmd_num = stack_cmd.split()
    if "push" in stack_cmd:
        stack.push(int(cmd_num[1]))

    if "top" in stack_cmd:
        stack.peek()

    if "pop" in stack_cmd:
        stack.pop()

    if "size" in stack_cmd:
        stack.size()

    if "empty" in stack_cmd:
        stack.is_empty()
