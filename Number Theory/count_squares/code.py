class Solution:
    def countSquares(self, N):
        
        # The basic logic behind this is if given no is square root of N then
        # there are N numbers present whose square lies in range of 1 to no

        sqrt = N**0.5
        if int(sqrt)*int(sqrt)==N:
            return int(sqrt)-1
        else:
            return int(sqrt)