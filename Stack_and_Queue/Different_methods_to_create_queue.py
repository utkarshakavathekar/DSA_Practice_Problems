########################   Using python list   #####################################################################
### enqueue at end of list and dequeue from start of list

#create queue
queue1 = list()

# enqueue element at end
queue1.append(10)
queue1.append(20)
queue1.append(30)

#deque element from start of queue
queue1.pop(0)    #10 # pops element at given index here we will pop at 0 for dequeue
queue1.pop(0)    #20

#check if queue is empty
if not queue1:
    print("empty queue")

#to check element at end/rear
queue1[0]

#to check element at start/front
queue1[-1]


########################   Using python list   #####################################################################
### enqueue at start of list and dequeue from end of list

#create queue
queue1 = list()

#enqueue element at start using insert with index 0
queue1.insert(0,10)
queue1.insert(0,20)
queue1.insert(0,30)

#dequeue elelemnt from end using normal pop()
queue1.pop()   #10
queue1.pop()   #20

#check if queue is empty
if not queue1:
    print("empty queue")

#to check element at end/rear
queue1[-1]

#to check element at start/front
queue1[0]


####################### Using collections module  #################################################################
# deque is double ended queue which can be used as to create queue in 2 ways
# append() - insert at right end
# pop() -  remove from right end

# appendleft - insert at left end
# popleft - remove from left end
from collections import deque

# create queue
queue1  = deque()

#to pushing element at top use append method of queue
queue1.append(10)
queue1.append(20)
queue1.append(30)

# pop element at top of queue1 use pop()
queue1.popleft()  # returns 30
queue1.popleft()  # returns 20

#------------------------------------------------------- OR

#to pushing element at top use append method of queue
queue1.appendleft(10)
queue1.appendleft(20)
queue1.appendleft(30)

# pop element at top of queue1 use pop()
queue1.pop()  # returns 30
queue1.pop()  # returns 20


####################### Using queue libraray  #####################################################################
# queue which can be used as stack is called Queue

from queue import Queue

# create stack
queue1 = Queue()

#to enqueue element at use put method of Queue
queue1.put(10)
queue1.put(20)
queue1.put(30)

# dequeue element of queue1 using get()
queue1.get() # returns 10
queue1.get()  # returns 20

# if queue1 is empty then it will continue executing, we need to give timeout to stop search so that 
# it can give error queue1 empty
queue1.get(timeout=1)

# similarly if queue1 is of fixed size and after getting full you try to add ele then it continue executing, 
# need to give timeout so that it can raise error queue1 full
queue1.put(timeout=1)

# to check if queue1 is empty
if not queue1:
    print("queue1 is empty")

if len(queue1)==0:
    print("queue1 is empty")
