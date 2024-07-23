# 10828
import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        
    
    def pop(self):
        if self.empty() == 0:
            print(self.stack.pop())
        else:
            print(-1)

    def size(self):
        print(len(self.stack))

    def empty(self):
        if len(self.stack) <= 0: # 원소가 없으면 1
            return 1
        else:
            return 0 #원소가 있으면 0

    def top(self):
        if self.empty() == 0:
            print(self.stack[-1])
        else:
            print(-1)

if __name__=="__main__":
    n = int(sys.stdin.readline())

    stack_ = Stack()

    for _ in range(n):
        input_ = sys.stdin.readline().rstrip().split(' ')

        if input_[0] == 'push':
            stack_.push(int(input_[1]))

        elif input_[0] == 'pop':
            stack_.pop()
        
        elif input_[0] == 'size':
            stack_.size()

        elif input_[0] == 'empty':
            print(stack_.empty())

        elif input_[0] == 'top':
            stack_.top()