################# first approach using 2 queues ##############
class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        

    def push(self, x: int) -> None:
        self.queue2.append(x)

        while self.queue1 !=[]:
            ele = self.queue1.pop(0)
            self.queue2.append(ele)

        while self.queue2 !=[]:
            ele = self.queue2.pop(0)
            self.queue1.append(ele)
        

    def pop(self) -> int:

        if self.queue1==[]:
            return -1
        else:
            return self.queue1.pop(0)
        

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        if self.queue1==[]:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

######################### second approach using single queue ##############################

class MyStack:

    def __init__(self):
        self.queue1 = []
        

    def push(self, x: int) -> None:
        self.queue1.append(x)

        for i in range(0,len(self.queue1)-1):
            ele = self.queue1.pop(0)
            self.queue1.append(ele)
        

    def pop(self) -> int:
        if self.queue1==[]:
            return -1
        else:
            return self.queue1.pop(0)     

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        if self.queue1==[]:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

