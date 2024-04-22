class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        low=1
        high= len(arr)-2
        if len(arr)==1:
            return arr[0]
        if arr[0]!=arr[1]:
            return arr[0]
        if arr[len(arr)-1]!=arr[high]:
            return arr[len(arr)-1]
        while low<=high:
            mid = int((low+high)//2)

            if mid%2==1:
                if arr[mid]==arr[mid-1]:
                    low=mid+1
                elif arr[mid]==arr[mid+1]:
                    high = mid-1
                else:
                    return arr[mid]
            else:
                if arr[mid]==arr[mid+1]:
                    low=mid+1
                elif arr[mid]==arr[mid-1]:
                    high = mid-1
                else:
                    return arr[mid]

            
        
            
        