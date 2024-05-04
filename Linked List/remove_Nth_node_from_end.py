# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        end_ptr = head
        Nth_ptr = head

        cnt = 0
        while cnt!=n and end_ptr!=None:
            cnt+=1
            end_ptr = end_ptr.next

        if end_ptr == None:
            head = head.next
            return head


        while end_ptr!=None and end_ptr.next !=None:
            end_ptr = end_ptr.next
            Nth_ptr = Nth_ptr.next

        Nth_ptr.next = Nth_ptr.next.next
        return head
