#User function Template for python3

class MyQueue:
    def __init__(self):
        self.queue = []
    
    #Function to push an element x in a queue.
    def push(self, x):
        self.queue.append(x)
         
         #add code here
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if self.queue == []:
            return -1
        else:
            return self.queue.pop(0)
         
         # add code here


#User function Template for python3

class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        self.arr.append(data)
    
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        if self.arr == []:
            return -1
        else:
            return self.arr.pop()
        
        

