'''Stack implementation using Python List'''

# class Stack:
#     def __init__(self):
#         self.s = []
#     def push(self,val):
#         self.s.append(val)
#     def is_empty(self):
#         return len(self.s) == 0
#     def pop(self):
#         if self.is_empty():
#             return "Stack is empty"
#         return self.s.pop()
#     def size(self):
#         if self.is_empty():
#             return 0
#         return len(self.s)
#     def peek(self):
#         if self.is_empty():
#             return "Stack is empty"
#         return self.s[-1]
# st = Stack()
# print(st.is_empty())
# st.push(20)
# st.push(30)
# st.push(40)
# st.push(50)
# st.push(60)
# print(st.is_empty())
# print(st.pop())
# print(st.pop())
# print(st.size())
# print(st.peek())


'''Stack implementation using Linked List'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack_LL:
    def __init__(self):
        self.top = None
    def push(self,val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
    def is_empty(self):
        return self.top is None
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        temp = self.top.next
        self.top.next = self.top.next.next
        del temp