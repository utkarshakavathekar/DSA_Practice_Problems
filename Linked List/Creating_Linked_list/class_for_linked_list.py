class Node():

    def __init__(self,value=0):
        self.val=value
        self.next = None

class LinkedList():

    def __init__(self):
        self.head = None

    def addNodeEnd(self,val):
        ptr = self.head
        if ptr==None:
            n1 = Node(val)
            self.head=n1
        else:
            while ptr.next!=None:
                ptr=ptr.next
            n1=Node(val)
            ptr.next = n1
    
    def traverseList(self):
        ptr=self.head
        if ptr==None:
            print("Empty list")
        else:
            while ptr!=None:
                print(ptr.val)
                ptr=ptr.next
    

if __name__=='__main__':
    l1 = LinkedList()
    l1.traverseList()
    l1.addNodeEnd(12)
    l1.addNodeEnd(13)
    l1.addNodeEnd(14)
    l1.traverseList()