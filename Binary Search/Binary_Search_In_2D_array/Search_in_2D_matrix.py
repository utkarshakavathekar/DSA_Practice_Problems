class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N,M = len(matrix),len(matrix[0])
        low=0
        high = N*M-1

        while low<=high:
            mid=int((low+high)//2)
            row=mid//M
            col=mid%M
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                high=mid-1
            else:
                low=mid+1
        return False

        