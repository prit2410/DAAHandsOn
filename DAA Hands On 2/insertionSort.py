def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Test Case 1: Random array
arr1 = [12, 11, 13, 5, 6]
print("Sorted array 1:", insertion_sort(arr1))

# Test Case 2: Already sorted array
arr2 = [1, 2, 3, 4, 5]
print("Sorted array 2:", insertion_sort(arr2))

# Test Case 3: Reverse sorted array
arr3 = [5, 4, 3, 2, 1]
print("Sorted array 3:", insertion_sort(arr3))

# Test Case 4: Array with all identical elements
arr4 = [7, 7, 7, 7, 7]
print("Sorted array 4:", insertion_sort(arr4))

# Test Case 5: Array with negative numbers
arr5 = [3, -1, 4, -5, 0]
print("Sorted array 5:", insertion_sort(arr5))
