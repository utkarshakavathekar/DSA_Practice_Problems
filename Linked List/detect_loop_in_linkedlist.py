# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        reached = []
        cycle = False
        if head==None:
            return cycle
        while head.next!=None:
            if head not in reached:
                reached.append(head)
                head=head.next
            else:
                cycle = True
                break
        return cycle