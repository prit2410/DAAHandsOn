def remove_duplicates(arr):
    if not arr:
        return []

    # Index of the next unique element
    j = 0

    # Traverse the array starting from the second element
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]

    # Return the array up to the point where unique elements are stored
    return arr[:j + 1]


# Example usage:
array1 = [2, 2, 2, 2, 2]
array2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]

print(remove_duplicates(array1))
# Output: [2]

print(remove_duplicates(array2))
# Output: [1, 2, 3, 4, 5]
