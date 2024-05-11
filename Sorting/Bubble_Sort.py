 def bubbleSort(self,arr, n):
    for i in range(0,len(arr)-1):
        sorted=True
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                sorted=False
        if sorted==True:
            break
    return arr