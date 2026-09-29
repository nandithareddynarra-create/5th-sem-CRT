'''singly linked list
Algorithm:
1. Creating Nodes
2. Insert the data
3. Connection between the nodes
4. Traverse each node'''

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# def traverse():
#     curr = node1
#     while curr:
#         print(curr.data, end = " -> ")
#         curr = curr.next
#     print("None")
# traverse()


# OPERATIONS:
# 1. Insertion
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


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# -------------------------------------------------
# 1(a). INSERTION AT THE BEGINNING
# -------------------------------------------------
def insert_begin(head, data):
    new_node = Node(data)

    new_node.next = head

    return new_node


# -------------------------------------------------
# 1(b). INSERTION AT THE END
# -------------------------------------------------
def insert_end(head, data):
    new_node = Node(data)

    # If linked list is empty
    if head is None:
        return new_node

    curr = head

    # Move to the last node
    while curr.next:
        curr = curr.next

    # Add new node at the end
    curr.next = new_node

    return head


# -------------------------------------------------
# 1(c). INSERTION AFTER A PARTICULAR NODE
# -------------------------------------------------
def insert_after(head, key, data):
    curr = head

    # Search for the particular node
    while curr:
        if curr.data == key:

            new_node = Node(data)

            new_node.next = curr.next
            curr.next = new_node

            return head

        curr = curr.next

    print("Node not found")
    return head


# -------------------------------------------------
# 2(a). DELETION AT THE BEGINNING
# -------------------------------------------------
def deletion_begin(head):

    # If linked list is empty
    if head is None:
        print("Error: List is empty")
        return None

    new_head = head.next

    # Delete first node
    del head

    return new_head


# -------------------------------------------------
# 2(b). DELETION AT THE END
# -------------------------------------------------
def deletion_end(head):

    # If linked list is empty
    if head is None:
        print("Error: List is empty")
        return None

    # If there is only one node
    if head.next is None:
        del head
        return None

    curr = head

    # Move to second-last node
    while curr.next.next:
        curr = curr.next

    # Delete last node
    del curr.next

    curr.next = None

    return head


# -------------------------------------------------
# 2(c). DELETION AFTER A PARTICULAR NODE
# -------------------------------------------------
def deletion_after(head, key):

    curr = head

    # Search for the particular node
    while curr:

        if curr.data == key:

            # If there is no node after the key
            if curr.next is None:
                print("No node exists after", key)
                return head

            temp = curr.next

            curr.next = temp.next

            del temp

            return head

        curr = curr.next

    print("Node not found")

    return head


# -------------------------------------------------
# 3. TRAVERSE
# -------------------------------------------------
def traverse(head):

    curr = head

    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next

    print("None")


# -------------------------------------------------
# 4. UPDATION
# -------------------------------------------------
def update(head, old_data, new_data):

    curr = head

    # Search for the node
    while curr:

        if curr.data == old_data:

            curr.data = new_data

            return head

        curr = curr.next

    print("Node not found")

    return head


# =================================================
# MAIN PROGRAM
# =================================================

head = None


# -------------------------------------------------
# INSERTION AT BEGINNING
# -------------------------------------------------

head = insert_begin(head, 10)
head = insert_begin(head, 20)
head = insert_begin(head, 30)

print("Insertion at beginning:")
traverse(head)

print()


# -------------------------------------------------
# INSERTION AT END
# -------------------------------------------------

head = insert_end(head, 100)

print("Insertion at end:")
traverse(head)

print()


# -------------------------------------------------
# INSERTION AFTER PARTICULAR NODE
# -------------------------------------------------

head = insert_after(head, 20, 50)

print("Insertion after node 20:")
traverse(head)

print()


# -------------------------------------------------
# DELETION AT BEGINNING
# -------------------------------------------------

head = deletion_begin(head)

print("Deletion at beginning:")
traverse(head)

print()


# -------------------------------------------------
# DELETION AT END
# -------------------------------------------------

head = deletion_end(head)

print("Deletion at end:")
traverse(head)

print()


# -------------------------------------------------
# DELETION AFTER PARTICULAR NODE
# -------------------------------------------------

head = deletion_after(head, 20)

print("Deletion after node 20:")
traverse(head)

print()


# -------------------------------------------------
# UPDATION
# -------------------------------------------------

head = update(head, 10, 500)

print("After updating 10 to 500:")
traverse(head)

print()   