# size = 5
# li = [0]*size
# print(li)

class Circular_Queue:
    def __init__(self,size):
        self.size = size
        self.queue = [None]*self.size
        self.front = -1
        self.rear = -1
    def enqueue(self,val):
        if self.front == (self.rear % self.size) +1:
            return "Queue is Empty"
        