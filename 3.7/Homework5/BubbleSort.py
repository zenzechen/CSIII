BubbleSort(arr):
    for i from 0 to length(arr) - 1:
        for j from 0 to length(arr) - i - 1:
            if arr[j] > arr[j + 1]:  
                swap(arr[j], arr[j + 1])