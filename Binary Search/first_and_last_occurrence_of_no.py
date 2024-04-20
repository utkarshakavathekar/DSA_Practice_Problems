class Solution:
    def searchRange(self, arr: List[int], x: int) -> List[int]:
        # O(N) approach
        # pos = [-1,-1]
        # if len(nums)==1 and nums[0]==target:
        #     return [0,0]
        # if nums==[]:
        #     return pos
        # if nums[-1]<target or nums[0]>target:
        #     return pos

        # for i in range(0,len(nums)):
        #     if nums[i]==target and pos[0]==-1:
        #         pos[0]=i
        #     if nums[i]!=target and pos[0]!=-1:
        #         pos[1]=i-1
        #         return pos
        # #print(i)
        # if i==len(nums)-1 and pos[0]!=-1:
        #     pos[1]=i
        # return pos

        # O(2logN) approach
        first,last = -1,-1
        n=len(arr)
        low=0
        high = n-1
        while low<=high:
            mid =int((low+high)//2)

            if arr[mid]==x:
                first=mid
                high =mid-1
            elif arr[mid]>x:
                high =mid-1
            else:
                low=mid+1
        low=0
        high = n-1
        while low<=high:
            mid =int((low+high)//2)

            if arr[mid]==x:
                last=mid
                low=mid+1
            elif arr[mid]<x:
                low=mid+1
            else:
                
                high =mid-1
        ans=[first,last]
        
        return ans

