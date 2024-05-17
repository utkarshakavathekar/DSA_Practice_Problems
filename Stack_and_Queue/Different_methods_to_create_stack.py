########################   Using python list   #####################################################################
#create stack
stack = list()

#create stack [10, 20, 30] by pushing element at top
stack.append(10)
stack.append(20)
stack.append(30)

# pop element at top of stack 
stack.pop()  # returns 30
stack.pop()  # returns 20

# to check if stack is empty
if not stack:
    print("stack is empty")

if len(stack)==0:
    print("stack is empty")

# to check the top element peak operation
peak = stack[-1]

####################### Using collections module  #################################################################
# deque is double ended queue which can be used as stack
from collections import deque

# create stack
stack  = deque()

#to pushing element at top use append method of queue
stack.append(10)
stack.append(20)
stack.append(30)

# pop element at top of stack use pop()
stack.pop()  # returns 30
stack.pop()  # returns 20

# to check if stack is empty
if not stack:
    print("stack is empty")

if len(stack)==0:
    print("stack is empty")

# to check the top element peak operation
peak = stack[-1]

####################### Using queue libraray  #####################################################################
# queue which can be used as stack is called LifoQueue

from queue import LifoQueue

# create stack
stack = LifoQueue()

#to pushing element at top use put method of LifoQueue
stack.put(10)
stack.put(20)
stack.put(30)

# pop element at top of stack use get()
stack.get() # returns 30
stack.get()  # returns 20

# if stack is empty then it will continue executing, we need to give timeout to stop search so that 
# it can give error stack empty
stack.get(timeout=1)

# similarly if stack is of fixed size and after getting full you try to add ele then it continue executing, 
# need to give timeout so that it can raise error stack full
stack.put(timeout=1)

# to check if stack is empty
if not stack:
    print("stack is empty")

if len(stack)==0:
    print("stack is empty")


