'''Queue Implementation Using Python List'''

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,val):
        self.queue.append(val)
    def is_empty(self):
        return len(self.queue) == 0
    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.queue.pop(0)
    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]
    def size(self):
        if self.is_empty():
            return 0
        return len(self.queue)
    def display(self):
        if self.is_empty():
            return "Queue is empty"
        for ele in self.queue:
            print(ele, end=" ")
qu = Queue()
print(qu.is_empty())
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
print(qu.is_empty())
print(qu.dequeue())
print(qu.front())
print(qu.size())
print(qu.display())