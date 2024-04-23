class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        N = len(mat)
        M = len(mat[0])

        low = 0
        high = M-1

        while low<=high:
            mid=int((low+high)//2)
            max_row = self.getMaxCol(mat,mid,N)
            print(max_row)

            left,right = -1,-1
            if mid-1>=0:
                left = mat[max_row][mid-1]
            if mid+1<M:
                right = mat[max_row][mid+1]

            if mat[max_row][mid]>left and mat[max_row][mid]>right:
                return [max_row,mid]

            elif mat[max_row][mid]<left:
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]


    def getMaxCol(self,mat,col,N):
        maxno = mat[0][col]
        index = 0
        for i in range(N):
            if mat[i][col]>maxno:
                maxno=mat[i][col]
                index = i
        return index

        