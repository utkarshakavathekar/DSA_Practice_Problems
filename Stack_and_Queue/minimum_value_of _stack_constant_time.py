########################### using extra value min while storing any coming value (val,min_till_now)
from collections import deque
class MinStack:

    def __init__(self):
        self.stack = []  

    def push(self, val: int) -> None:
        if self.stack !=[]:
            stack_min = self.stack[-1][1]
        else:
            stack_min = None

        if stack_min==None or stack_min>val:
            self.stack.append((val,val))
        else:
            self.stack.append((val,stack_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        #print(self.stack)
        ans = self.stack[-1]
        return ans[1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



############################## using mini valriable and formula 2*val-mini for push, and 2*mini-poped_val for pop.
from collections import deque
class MinStack:

    def __init__(self):
        self.stack = []  
        self.mini = float('inf')

    def push(self, val: int) -> None:
        if self.stack==[]:
            self.mini = val
            self.stack.append(val)
        else:
            if val<self.mini:
                ins_val = 2*val-self.mini
                self.mini = val
                self.stack.append(ins_val)
            else:
                self.stack.append(val)

    def pop(self) -> None:
        curr_val = self.stack.pop()
        if curr_val<self.mini:
            self.mini = 2*self.mini-curr_val
        

    def top(self) -> int:
        top_val = self.stack[-1]
        if top_val<self.mini:
            return self.mini
        else:
            return top_val

    def getMin(self) -> int:
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()