class Node():

    def __init__(self,value=0):
        self.val=value
        self.next = None

class LinkedList():

    def __init__(self):
        self.head = None

    def insertNodeEnd(self,val):
        ptr = self.head
        if ptr==None:
            n1 = Node(val)
            self.head=n1
        else:
            while ptr.next!=None:
                ptr=ptr.next
            new=Node(val)
            ptr.next = new
    
    def insertNodeStart(self,val):
        if self.head== None:
            newNode = Node(val)
            self.head = newNode
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
        return self.head

    def insertAtKthPosition(self,val,k):
        if self.head == None:
            if k==1:
                newNode = Node(val)
                self.head = newNode
            else:
                print("cant insert at %d position"%k)
        else:
            if k==1:
                newNode = Node(val)
                newNode.next = self.head
                self.head = newNode
            else:
                ptr = self.head
                cnt=0
                while ptr.next !=None:
                    cnt+=1
                    if cnt==k-1:
                        newNode = Node(val)
                        newNode.next = ptr.next
                        ptr.next = newNode
                    ptr=ptr.next
                if cnt==k-2:
                    newNode = Node(val)
                    newNode.next = ptr.next
                    ptr.next = newNode
        return self.head

    def insertBeforeValK(self,val,k):
        if self.head == None:
            print("cant insert before %d"%k)
        else:
            if self.head.val==k:
                newNode = Node(val)
                newNode.next = self.head
                self.head = newNode
            else:
                ptr = self.head
                
                while ptr.next !=None:
                    if ptr.next.val==k:
                        newNode = Node(val)
                        newNode.next = ptr.next
                        ptr.next = newNode
                        break
                    ptr=ptr.next
                
        return self.head


    def traverseList(self):
        ptr=self.head
        if ptr==None:
            print("Empty list")
        else:
            while ptr!=None:
                print(ptr.val)
                ptr=ptr.next

    def deleteStartNode(self):
        if self.head==None:
            return self.head
        else:
            self.head = self.head.next
            return self.head
    
    def deleteEndNode(self):
        if self.head==None or self.head.next==None:
            self.head = None
            return self.head
        else:
            tmp = self.head
            while tmp.next.next !=None:
                tmp =tmp.next
            tmp.next = None
            return self.head

    def deleteKthNode(self,k):
        if k==0:
            return self.head
        if k==1:
            return self.deleteStartNode()
        else:
            cnt=0
            ptr=self.head
            prev = ptr.next
            while ptr.next != None:
                cnt+=1
                if cnt==k-1:
                    tmp = ptr.next
                    ptr.next = ptr.next.next
                    tmp.next = None
                    break
                ptr = ptr.next
            return self.head
    
    def deleteXdataNode(self,val):
        if self.head==None:
            return self.head
        if self.head.val == val:
            return self.deleteStartNode()
        else:
            ptr=self.head
            prev = ptr
            ptr=ptr.next
            while  ptr!=None:
            
                if ptr.val==val:
                    prev.next = prev.next.next
                    break
                ptr = ptr.next
                prev=prev.next
            return self.head



if __name__=='__main__':
    l1 = LinkedList()
    #l1.insertAtKthPosition(100,0)
    #l1.insertBeforeValK(100,12)
    l1.traverseList()
    l1.insertNodeEnd(12)
    l1.insertNodeEnd(13)
    l1.insertNodeEnd(14)
    l1.insertNodeEnd(15)
    l1.traverseList()
    #l1.insertAtKthPosition(100,0)
    l1.insertBeforeValK(100,13)
    print("------------")
    l1.traverseList()
    
    # l1.deleteKthNode(5)
    # l1.deleteXdataNode(12)
    # l1.traverseList()
    # print("------------")
    # l1.deleteStartNode()
    # l1.traverseList()
    # print("------------")
    # l1.deleteEndNode()
    # l1.deleteEndNode()
    # l1.traverseList()
    # l1.insertNodeStart(1)
    # l1.traverseList()
    # l1.insertNodeStart(2)
    # l1.traverseList()
    