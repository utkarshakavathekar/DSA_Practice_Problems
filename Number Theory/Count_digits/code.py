class Solution:
    def evenlyDivides (self, N):
        cnt=0
        tmp=N
        
        while tmp>0:
            dig = tmp%10
            
            if dig!=0 and N%dig==0:
                cnt+=1
            tmp//=10
        return cnt
