#Function to sort the list using insertion sort algorithm.
def insertionSort(self, alist, n):
    #code here
    if n<=1:
        return alist
    for i in range(1,n):
        val = alist[i]
        j = i-1
        while j>=0 and val<alist[j]:
            alist[j+1]=alist[j]
            j-=1
        alist[j+1]=val
    return alist
