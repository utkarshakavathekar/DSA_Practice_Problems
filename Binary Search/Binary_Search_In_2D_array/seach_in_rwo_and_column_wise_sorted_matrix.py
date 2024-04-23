class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N=len(matrix)
        M=len(matrix[0])
        row=0
        col=M-1
        while row<N and col>-1:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                col-=1
            else:
                row+=1
        return False


    #     time required O(NlogM) better approach
    #     N=len(matrix)
    #     M=len(matrix[0])
    #     found=False
    #     for i in range(N):
    #         ans = self.binarySearch(matrix[i],target)
    #         if ans:
    #             found=True
    #             return found
    #     return found

    # def binarySearch(self,arr,target):
    #     low=0
    #     high = len(arr)-1

    #     while low<=high:
    #         mid=int((low+high)//2)
    #         if arr[mid]==target:
    #             return True
    #         elif arr[mid]>target:
    #             high=mid-1
    #         else:
    #             low=mid+1
    #     return False