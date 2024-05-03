# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:

        slow = head
        fast = head
        while fast!=None and fast.next !=None:
            slow=slow.next
            fast=fast.next.next
        rev_mid = self.reverse(slow)
    
        start = head
        while rev_mid!=None:
            if start.val==rev_mid.val:
                start=start.next
                rev_mid = rev_mid.next
            else:
                return False
        return True

        
    def reverse(self,head):
        if head==None or head.next==None:
            return head

        newHead = self.reverse(head.next)
        front = head.next
        front.next = head
        head.next = None
        print(head.val)
        return newHead
        