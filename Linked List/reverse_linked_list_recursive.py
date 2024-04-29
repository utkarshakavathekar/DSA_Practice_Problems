# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        if head==None or head.next==None:
            return head
        newHead = self.reverseList(head.next)
        # VIMP step - as head in current iteration is still pointing to front of reversed part
        # we can use it to reach front of reversed list were next node will be attached
        #  1-->2-->3---> 4<--5   <-newHead
        #        head    |
        #                V
        #               None
        front = head.next
        front.next = head
        head.next = None
        return newHead


        