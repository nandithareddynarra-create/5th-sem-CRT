class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None
class double():
    def __init__(self):
        self.head =  None
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head 
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        return new_node
    
    def count_nodes(self):
        if self.head is None:
            return 0
        if self.head.next is None:
            return 1
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
        
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            return new_node
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr.next

    # def insert_at_pos(self,data,pos):
    #     new_node = Node(data)
    #     if self.head is None:
    #         return 
    #     count = self.count_nodes()
    #     if len(count) < pos:
    #         return
    #     if pos is 0:
    #         self.insert_at_beginning()
    #         temp = self.head
    #     new_node.prev = temp
    #     new_node.next = temp.next
    #     temp.next = new_node
    #     temp.next.prev = new_node

    def insert_at_pos(self, data, pos):
        new_node = Node(data)
        if self.head is None:
            return
        if pos == 0:
            self.insert_at_beginning(data)
            return
        count = self.count_nodes()
        if pos < 0 or pos >= count:
            return
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next
        new_node.prev = temp
        new_node.next = temp.next
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node

    def del_at_biginning(self,data):
        if self.head is None:
            return
        del_node = self.head
        self.head = self.head.next
        del del_node

    def del_at_end(self,data):
        if self.head is None:
            return
        temp = self.head
        if temp.next is None:
            self.head = None
            return
        while temp.next.next:
            temp = temp.next
            del_node = temp.next
        temp.next.prev = None
        temp.next = None
        del del_node


    def del_at_pos(self, pos):
        if self.head is None:
            return
        # Delete first node
        if pos == 0:
            temp = self.head
            self.head = temp.next

            if self.head is not None:
                self.head.prev = None

            del temp
            return

        temp = self.head 
        # Move to the node at position
        for i in range(pos):
            if temp is None:
                return
            temp = temp.next

        # Position doesn't exist
        if temp is None:
            return

        # Connect previous node to next node
        temp.prev.next = temp.next

        # Connect next node to previous node
        if temp.next is not None:
            temp.next.prev = temp.prev

        del temp



    def traverse(self):
        if not self.head:
            return
        temp = self.head
        while temp:
            print(temp.data , end = " <-> ")
            temp = temp.next
        print("None")

dll = double()
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_beginning(30)
dll.traverse()
dll.insert_at_end(40)
dll.insert_at_end(50)
dll.traverse()
print(dll.count_nodes())
dll.insert_at_pos(60,2)
dll.traverse()
dll.del_at_biginning(30)
dll.traverse()
dll.del_at_end(50)
dll.traverse()