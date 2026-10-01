'''Queue Implementation using Linked List'''

'''Time complexity for enqueue, dequeue operations - O(1)'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue_LL:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,val):
        new_node = Node(val)
        if self.rear is None:
            self.rear = self.front = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        temp = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rare == None
        return temp
    def front_(self):
        if self.front is None:
            return "Queue is Empty"
        return self.front.data
    def display(self):
        if self.front is None:
            print("Queue is Empty")
        temp = self.front
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        print()
qu = Queue_LL()
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
qu.enqueue(40)
qu.enqueue(50)
print(qu.dequeue())
print(qu.front_())
qu.display()