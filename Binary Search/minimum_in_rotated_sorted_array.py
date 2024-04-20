class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = 5001
        low=0
        high= len(nums)-1
        while low<=high:
            mid = int((low+high)//2)

            if nums[low]<=nums[mid]:
                if nums[low]<min_val:
                    min_val=nums[low]
                low=mid+1
            else:
                if nums[mid]<min_val:
                    min_val = nums[mid]
                high=mid-1
        return min_val
            
                