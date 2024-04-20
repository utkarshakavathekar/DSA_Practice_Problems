#This solution is for array having duplicate elements

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums)-1
        index=-1

        while low<=high:
            mid = int((low+high)//2)

            if nums[mid]==target:
                index=mid
                break

            if nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
                continue
            if nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        if index==-1:
            return False
        else:
            return True
        