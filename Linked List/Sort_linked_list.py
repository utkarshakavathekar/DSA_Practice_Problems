# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        return self.mergeSort(head)
        
    def merge(self,left,right):
        l=left
        r=right
        head = ListNode(-1)
        tmp = head
        
        while l!=None and r!=None:
            
            if l.val<r.val:
                tmp.next = l
                l=l.next
                tmp=tmp.next
            else:
                tmp.next=r
                r=r.next
                tmp=tmp.next
            
        if l==None:
            tmp.next = r
        if r==None:
            tmp.next = l
            
        return head.next

    def findMiddle(self,head):
        slow = head
        fast = head.next

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow

    def mergeSort(self,head):
        if head==None or head.next==None:
            return head

        mid_head = self.findMiddle(head)
        print(mid_head.val)
        left = head
        right = mid_head.next
        mid_head.next = None

        left = self.mergeSort(left)
        right = self.mergeSort(right)
        head = self.merge(left,right)
        return head