import sys
input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.queue = []


    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if self.queue:
            q = self.queue[0]
            self.queue = self.queue[1:]
            return q
        else:
            return -1
    def size(self):
        return len(self.queue)

    def empty(self):
        if self.queue:
            return 0
        else:
            return 1

    def front(self):
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def back(self):
        if self.queue:
            return self.queue[-1]
        else:
            return -1


if __name__ == "__main__":
    n = int(input().rstrip())
    queue = Queue()
    for _ in range(n): 
       
        input_ = input().rstrip().split(' ')

        if input_[0] == 'push':
            queue.push(int(input_[1]))

        elif input_[0] == 'pop':
            print(queue.pop())

        elif input_[0] == 'size':
            print(queue.size())

        elif input_[0] == 'empty':
            print(queue.empty())

        elif input_[0] == 'front':
            print(queue.front())

        elif input_[0] == 'back':
            print(queue.back())


        
        

