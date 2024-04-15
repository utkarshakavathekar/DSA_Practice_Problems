class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        gcd = self.gcd(A,B)
        lcm = (A//gcd)*B
        return int(lcm),gcd
        
    def gcd(self,A,B):
        if B==0:
            return A
        else:
            return self.gcd(B,A%B)