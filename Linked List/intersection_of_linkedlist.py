# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        prev_node = set()
        tmp = headA
        while tmp!=None:
            prev_node.add(tmp)
            tmp = tmp.next

        tmp = headB
        while tmp!=None:
            if tmp in prev_node:
                return tmp
            tmp = tmp.next
        return None
        

        ##################################################
        l1,l2=0,0
        p1 = headA
        p2 = headB
        while p1!=None:
            l1+=1
            p1=p1.next
        while p2!=None:
            l2+=1
            p2=p2.next
        ptr1 = headA
        ptr2 = headB
        if l1>l2:
            diff = l1-l2
            while diff>0:
                print(ptr1.val)
                ptr1=ptr1.next
                diff-=1
        elif l2>l1:
            diff = l2-l1
            while diff>0:
                print(ptr2.val)
                ptr2=ptr2.next
                diff-=1
        
        while ptr1!=None:
            print(ptr1.val)
            print(ptr2.val)
            if ptr1==ptr2:
                return ptr1
            ptr1=ptr1.next
            ptr2=ptr2.next
        return ptr1
