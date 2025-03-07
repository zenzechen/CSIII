SelectionSort(arr):
    for i from 0 to length(arr) - 1:
        min_index = i
        for j from i + 1 to length(arr):
            if arr[j] < arr[min_index]:  
                min_index = j
        swap(arr[i], arr[min_index]) 