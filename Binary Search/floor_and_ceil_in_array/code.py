def getFloorAndCeil(arr, n, x):
    # Write your code here.
    floor,ceil = -1,-1
    low=0
    high = n-1
    while low<=high:
        mid =int((low+high)//2)

        if arr[mid]>=x:
            ceil=mid
            high =mid-1
        else:
            low=mid+1
    low=0
    high = n-1
    while low<=high:
        mid =int((low+high)//2)

        if arr[mid]<=x:
            floor=mid
            low=mid+1
        else:
            
            high =mid-1
    ans=[-1,-1]
    if floor!=-1:
        ans[0]=arr[floor]
    if ceil!=-1:
        ans[1]=arr[ceil]
    return ans[0],ans[1]