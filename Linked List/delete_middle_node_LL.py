# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):
        if head==None or head.next==None:
            return None
        prev_mid = self.find_middle(head)
        prev_mid.next = prev_mid.next.next
        return head

    def find_middle(self,head):
        slow = head
        fast = head
        prev = head
        
        while fast!=None and fast.next!=None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev


        