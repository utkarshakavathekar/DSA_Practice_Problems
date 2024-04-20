
#This solution is for array having unique elements
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index=-1
        end_ptr=len(nums)-1
        
        index= self.binary_search(nums,0,end_ptr,target)
       
        if index is None:
            index=-1
        return index

    def binary_search(self,arr,strt,end,target):
        while strt<=end:
            mid = (strt+end)//2
            if arr[mid]==target:
                return mid

            # this means start to mid part is sorted
            if arr[strt]<=arr[mid]:
                #if search value present in this range
                if arr[strt]<=target<arr[mid]:
                    end=mid-1
                else:
                    strt=mid+1
            # else mid to end part is sorted
            else:
                #if search value present in this range
                if arr[mid]<target<=arr[end]:
                    strt=mid+1
                else:
                    end=mid-1
                
            
        