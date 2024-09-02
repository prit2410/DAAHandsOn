def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test Case 1: Random array
arr1 = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array 1:", bubble_sort(arr1))

# Test Case 2: Already sorted array
arr2 = [1, 2, 3, 4, 5]
print("Sorted array 2:", bubble_sort(arr2))

# Test Case 3: Reverse sorted array
arr3 = [5, 4, 3, 2, 1]
print("Sorted array 3:", bubble_sort(arr3))

# Test Case 4: Array with all identical elements
arr4 = [8, 8, 8, 8, 8]
print("Sorted array 4:", bubble_sort(arr4))

# Test Case 5: Array with negative numbers
arr5 = [3, -1, 4, -5, 0]
print("Sorted array 5:", bubble_sort(arr5))
