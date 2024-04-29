# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head):
        ptr_1step = head
        ptr_2step = head
        while ptr_2step.next != None:
            ptr_1step = ptr_1step.next
            ptr_2step = ptr_2step.next
            if ptr_2step.next !=None:
                ptr_2step = ptr_2step.next
        return ptr_1step