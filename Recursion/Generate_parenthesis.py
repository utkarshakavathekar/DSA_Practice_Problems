class Solution:
    def generateParenthesis(self, n):
        open_c = n
        close_c = n
        ans = []
        op = ''
        self.generate(open_c,close_c,op,ans)
        return ans
        

    def generate(self,open_c,close_c,op,ans):
        if open_c==0 and close_c==0:
            #print(ans)
            ans.append(op)
            return
        if open_c!=0:
            op1 = op + '('
            self.generate(open_c-1,close_c,op1,ans)

        if open_c < close_c:
            op2 = op + ')'
            self.generate(open_c,close_c-1,op2,ans)
        
        return
