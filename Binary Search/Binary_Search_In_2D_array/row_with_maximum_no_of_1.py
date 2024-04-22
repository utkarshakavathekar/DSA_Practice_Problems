def rowWithMax1s(matrix: [[int]], n: int, m: int) -> int:
    max_cnt=-1
    index=-1

    for i in range(0,n):
        curr_cnt = getFirstOccurrence(matrix[i],m)
        if curr_cnt>max_cnt:
            max_cnt=curr_cnt
            index=i
    return index

    
def getFirstOccurrence(arr,m):
    low=0
    high=m-1

    index=-1
    while low<=high:
        mid = int((low+high)//2)

        if arr[mid]==1:
            index=mid
            high=mid-1
        else:
            low=mid+1
    if index!=-1:
        return m-index
    else:
        return index