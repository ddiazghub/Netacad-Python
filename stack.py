class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        return self.__stack.pop()

    def peek(self):
        return self.__stack[-1]

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, value):
        self.__sum += value
        Stack.push(self, value)

    def pop(self):
        self.__sum -= Stack.peek(self)
        return Stack.pop(self)

    def get_sum(self):
        return self.__sum

stack = AddingStack()

for i in range(5):
    stack.push(i)
print(stack.get_sum())

for i in range(5):
    print(stack.pop())
