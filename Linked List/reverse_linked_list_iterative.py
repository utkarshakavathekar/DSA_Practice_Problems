# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        
        prev_node = None
        current_node = head
        nxt = None

        while current_node != None:
            nxt = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = nxt

        return prev_node
        