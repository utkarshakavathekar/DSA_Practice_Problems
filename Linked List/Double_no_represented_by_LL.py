# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head):
        c = self.doubleNode(head)
        if c==0:
            return head
        else:
            newNode = ListNode(c)
            newNode.next = head
            return newNode

    def doubleNode(self, head):
        if head==None or head.next==None:
            val = head.val*2
            carry = int(val//10)
            head.val = val%10
            return carry
        carry = self.doubleNode(head.next)
        val = head.val*2
        val = val +carry
        carry = int(val//10)
        head.val = val%10
        return carry
        