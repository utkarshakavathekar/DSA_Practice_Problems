class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
            # code here
            if low<high:
                part_index = self.partition(arr,low,high)
                self.quickSort(arr,low,part_index-1)
                self.quickSort(arr,part_index+1,high)
    
    def partition(self,arr,low,high):
        # code here
        pivot = low
        ptr1=low
        ptr2=high
        while ptr1<ptr2:
            while arr[ptr1]<=arr[pivot] and ptr1<high:
                ptr1+=1
            while arr[ptr2]>arr[pivot] and ptr2>low:
                ptr2-=1
            if ptr1<ptr2:
                arr[ptr1],arr[ptr2] = arr[ptr2],arr[ptr1]
    
        arr[ptr2],arr[pivot]=arr[pivot],arr[ptr2]
        return ptr2
    