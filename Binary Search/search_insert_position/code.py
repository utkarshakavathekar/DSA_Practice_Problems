class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high = len(nums)-1
        index=-1

        while low<=high:
            mid = int((low+high)//2)

            if nums[mid]==target:
                #if no found in array return its index
                index=mid
                return index
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        # if no not found in array then always the index pointed by low is insert index
        return low
        