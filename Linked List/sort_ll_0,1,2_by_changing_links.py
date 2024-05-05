class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def sortList(head):
    d_zero = Node(-1)
    d_one = Node(-1)
    d_two = Node(-1)

    zero,one,two = d_zero, d_one, d_two

    tmp = head
    while tmp!=None:
        if tmp.data == 0:
            zero.next = tmp
            tmp = tmp.next
            zero=zero.next
        elif tmp.data == 1:
            one.next = tmp
            tmp = tmp.next
            one=one.next
        else:
            two.next = tmp
            tmp = tmp.next
            two=two.next

    if d_zero.next==None:
        if d_one.next==None:
            head = d_two.next
        elif d_two.next ==None:
            head = d_one.next
            one.next = None
    elif d_one.next == None:
        head = d_zero.next
        if d_two.next ==None:
            zero.next = None
        else:
            zero.next = d_two.next
    elif d_two.next == None:
        head = d_zero.next
        zero.next = d_one.next
        one.next = None
    else:
        head = d_zero.next
        zero.next = d_one.next
        one.next = d_two.next
        two.next = None
    return head


