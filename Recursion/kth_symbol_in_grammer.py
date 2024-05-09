class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        
        mid = 2**(n-2)

        if k<=mid:
            bit = self.kthGrammar(n-1,k)
        else:
            bit = self.kthGrammar(n-1,k-mid)
            bit = 1-bit
        return bit