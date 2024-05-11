def selection_sort(arr, n):
    for i  in range(0,n):
        mini = i
        for j in range(i + 1,n):
            if (arr[j] < arr[mini]):
                mini = j
        #swap
        temp = arr[mini]
        arr[mini] = arr[i]
        arr[i] = temp