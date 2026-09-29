# '''876. Middle of the Linked List'''

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# def middleNode(head: ListNode | None) -> ListNode | None:
# #     if head is None:
# #         return None
# #     temp = head
# #     count = 0
# #     while temp:
# #         count += 1
# #         temp = temp.next
# #     middleIndex = count//2
# #     curr = head
# #     for i in range(middleIndex):
# #         curr = curr.next
# #     return curr
# # head = [1,2,3,4,5]
# # print(middleNode(head))


# # solution-2 (slow and fast pointer approach)  

#     slow = head
#     fast = head
#     while (fast and fast.next):
#         fast = fast.next.next
#         slow = slow.next
#     return slow



'''141. Linked List Cycle'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# from typing import Optional
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
        # visited = set()
        # curr = head
        # while curr:
        #     if curr in visited:
        #         return True
        #     visited.add(curr)
        #     curr = curr.next
        # return False

        # slow = head
        # fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if fast == slow:
        #         return True
        # return False


''' 21 Merge Two Sorted Lists '''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
#         # if list1 and list2 is None:
#         #     return []
#         # if not list1:
#         #     return list2
#         # if not list2:
#         #     return list1
#         temp = ListNode()
#         curr = temp
#         while list1 and list2:
#             if list1.val <= list2.val:
#                 curr.next = list1
#                 list1 = list1.next
#             else:
#                 curr.next = list2
#                 list2 = list2.next
#             curr = curr.next
#         if list1:
#             curr.next = list1
#         else:
#             curr.next = list2
#         return temp.next


'''206. Reverse Linked List'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: ListNode | None) -> ListNode | None:
#         prev = None
#         curr = head
        
#         while curr:
#             next_node = curr.next 
#             curr.next = prev       
#             prev = curr            
#             curr = next_node   
            
#         return prev

''''''