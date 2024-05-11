class Solution:
    def merge(self,arr, l, m, r): 
        ptr1=l
        ptr2=m
        tmp=[]
        while ptr1<m and ptr2<=r:
            if arr[ptr1]<arr[ptr2]:
                tmp.append(arr[ptr1])
                ptr1+=1
            else:
                tmp.append(arr[ptr2])
                ptr2+=1
        while ptr1<m:
            tmp.append(arr[ptr1])
            ptr1+=1
        while ptr2<=r:
            tmp.append(arr[ptr2])
            ptr2+=1
        j=0
        for i in range(l,r+1):
            arr[i]=tmp[j]
            j+=1

def mergeSort(self,arr, l, r):
    if l==r:
        return
    mid=(l+r)//2
    #print("l",l," mid",mid," r",r)
    self.mergeSort(arr,l,mid)
    self.mergeSort(arr,mid+1,r)
    self.merge(arr,l,mid+1,r)
