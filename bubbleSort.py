import numpy as np

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = np.array([45, 11, 23, 8, 39, 15, 30, 50, 22, 12])
bubbleSort(arr)
print(f"The bubble sorted array is: {arr}")