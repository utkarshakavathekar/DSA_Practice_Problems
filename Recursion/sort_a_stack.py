class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        # Code here
        if len(s)==1:
            return 
        top_ele = s.pop()
        self.Sorted(s)
        
        self.insertSorted(s,top_ele)
        return
        
    def insertSorted(self,s,val):
        if len(s)==0 or s[-1]<=val:
            s.append(val)
            return
        top_ele = s.pop()
        self.insertSorted(s,val)
        s.append(top_ele)
        return
        

