class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low=0
        l=len(nums)
        high = l-1
        if l==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[high]>nums[high-1]:
            return high

        low=1
        high=high-1
        while low<=high:
            mid = int((low+high)//2)
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid

            if nums[mid-1]<nums[mid]:
                low=mid+1
            else:
                high=mid-1
        