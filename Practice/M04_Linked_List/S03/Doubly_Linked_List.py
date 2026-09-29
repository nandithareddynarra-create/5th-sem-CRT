'''Double Linked List
The data can be stored in the node
Nodes ---> 3 parts
1. data
2. prev
3. next

***Algortithm***

1. Create node
2. insert data
3. connection
4. traverse

'''

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)

# node1.next = node2
# node2.prev = node1

# node2.next = node3
# node3.prev = node2

# node3.next = node4
# node4.prev = node3

# def traverse_forward():
#     curr = node1
#     while curr:
#         print(curr.data , end = " <-> ")
#         curr = curr.next
#     print("None")
# traverse_forward()

# def traverse_backward():
#     curr = node4
#     while curr:
#         print(curr.data , end = " <-> ")
#         curr = curr.prev
#     print("None")
# traverse_backward()


'''Operations
1. Insertion
#    a. Insertion at the beginning
#    b. Insertion at the end
#    c. Insertion after a particular node
#
# 2. Deletion
#    a. Deletion at the beginning
#    b. Deletion at the end
#    c. Deletion after a particular node
#
# 3. Traverse
#
# 4. Updation
'''

# insertion if a node at the beginning

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

# insertion at beginning

def insert_at_beginning(head,data):
    new_node = Node(data)
    new_node.next = head 
    if head:
        head.prev = new_node
    return new_node

# insertion at the end

def insert_at_end(head,data):
    new_node = Node(data)
    if head is None:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    new_node.prev = curr.next
    return head

# insertion after node

def insert_after_node(head,key,data):
    curr = head
    while curr and curr.data != key:
        curr = curr.next

    if curr is None:
        return head

    new_node = Node(data)
    new_node.prev = curr
    new_node.next = curr.next
    if curr.next:
        curr.next.prev = new_node
    curr.next = new_node
    return head

'''traversing'''

'''Insertion at beginning'''

def traverse(head):
    curr = head
    while curr:
        print(curr.data, end = " <->")
        curr = curr.next
    print("None")
head = None
head = insert_at_beginning(head,50)
head = insert_at_beginning(head,60)
head = insert_at_beginning(head,70)
print("Insertion at beginning")
traverse(head)
print() 

'''Insertion at ending'''
head = insert_at_end(head, 100)

print("Insertion at end:")
traverse(head)

print()
