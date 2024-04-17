class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # iterative approach
        # low = 0
        # high = len(nums)-1

        # while low<=high:
        #     mid = (low+high)//2

        #     if nums[mid]==target:
        #         return mid
        #     elif nums[mid]>target:
        #         high = mid-1
        #     else:
        #         low=mid+1
        # return -1

        # recursive approach
        low = 0
        high = len(nums)-1

        index = self.BinarySearch(nums,low,high,target)
        return index

    def BinarySearch(self,nums,low,high,target):

        if low>high:
            return -1
        mid = (low+high)//2

        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            return self.BinarySearch(nums,low,mid-1,target)  
        else:
            return self.BinarySearch(nums,mid+1,high,target)
            
        