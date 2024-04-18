# lower bound is a smallest no among all present which is just greater than or equal to target
def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    low = 0
    high = n-1
    index = n
    while low<=high:
        mid =int((low+high)//2)

        if arr[mid]>=x:
            index=mid
            high =mid-1
        else:
            low=mid+1
    return index

# upper bound is a smallest no among all present which is strcitly greater than target
def upperBound(arr: [int], x: int, n: int) -> int:
    low = 0
    high = n-1
    index = n
    while low<=high:
        mid =int((low+high)//2)

        if arr[mid]>x:
            index=mid
            high =mid-1
        else:
            low=mid+1
    return index