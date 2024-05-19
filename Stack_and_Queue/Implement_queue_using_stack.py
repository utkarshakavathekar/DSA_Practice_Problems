#3##################### using 2 stacks and O(N) for push
class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.head = 0
        self.tail=0
        

    def push(self, x: int) -> None:
        while len(self.stack1):
            top_ele = self.stack1.pop()
            self.stack2.append(top_ele)
        self.stack1.append(x)
        while len(self.stack2):
            top_ele = self.stack2.pop()
            self.stack1.append(top_ele)
        

    def pop(self) -> int:
        return self.stack1.pop()
        

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        if len(self.stack1)==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

#3##################### using 2 stacks and O(1) for push   ######################################
class MyQueue:

    def __init__(self):
        self.ipStack = []
        self.opStack = []

    def push(self, x: int) -> None:
        self.ipStack.append(x)
        

    def pop(self) -> int:
        if self.opStack !=[]:
            return self.opStack.pop()
        else:
            if self.ipStack ==[]:
                return -1
            while self.ipStack !=[]:
                self.opStack.append(self.ipStack.pop()) 
            return self.opStack.pop()

    def peek(self) -> int:
        if self.opStack !=[]:
            return self.opStack[-1]
        else:
            if self.ipStack ==[]:
                return -1
            while self.ipStack !=[]:
                self.opStack.append(self.ipStack.pop()) 
            return self.opStack[-1]

    def empty(self) -> bool:
        if len(self.opStack)==0 and len(self.ipStack)==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()