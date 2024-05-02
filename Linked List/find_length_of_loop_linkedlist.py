class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Please do not change code above.


def lengthOfLoop(head: Node) -> int:
    # Write your code here
    slow = head
    fast = head
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            # means cycle in linkedlist
            start = fast
            cnt = 1
            slow=slow.next
            while start != slow:
                cnt+=1
                slow = slow.next
            return cnt
    return 0
