# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head):
        cnt_ptr = head
        end_ptr = head
        tmp = head
        cnt=0
        if k==0 or head==None or head.next==None:
            return head
        while tmp!=None:
            cnt+=1
            tmp=tmp.next
        k = k%cnt
        if k==0 or head==None or head.next==None:
            return head
        while k>0:
            end_ptr=end_ptr.next
            k-=1
            
        while end_ptr.next!=None:
            cnt_ptr=cnt_ptr.next
            end_ptr=end_ptr.next

        new_head = cnt_ptr.next
        cnt_ptr.next = None
        end_ptr.next  = head
        return new_head

        