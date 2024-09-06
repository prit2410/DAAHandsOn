def merge_sort(arr):
    # Base case: if the array is of length 0 or 1, it's already sorted
    if len(arr) <= 1:
        return arr

    # Splitting the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    print(f"Splitting: {arr} -> {left} and {right}")

    # Recursively sorting both halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Merging the sorted halves
    merged = merge(left_sorted, right_sorted)
    print(f"Merging: {left_sorted} and {right_sorted} -> {merged}")
    return merged

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Merge the two halves in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from left or right
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

# Testing the merge sort on the provided array
array = [5, 2, 4, 7, 1, 3, 2, 6]
sorted_array = merge_sort(array)
print(f"Sorted array: {sorted_array}")
