# Partition function used in Quicksort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Quicksort implementation (not necessary to sort entire array for ith statistic)
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


# Function to find the ith order statistic
def ith_order_statistic(arr, low, high, i):
    if low == high:  # If the list contains only one element
        return arr[low]

    # Partition the array and get the position of the pivot element
    pi = partition(arr, low, high)

    # k is the number of elements on the left of the pivot including pivot itself
    k = pi - low + 1

    # If pivot is the ith element, return it
    if k == i:
        return arr[pi]
    elif i < k:
        # Recur on the left subarray if the ith element is on the left
        return ith_order_statistic(arr, low, pi - 1, i)
    else:
        # Recur on the right subarray if the ith element is on the right
        return ith_order_statistic(arr, pi + 1, high, i - k)


# Example usage
if __name__ == "__main__":
    arr = [12, 3, 5, 7, 19, 1]
    i = 4  # Find the 4th smallest element (ith order statistic)
    n = len(arr)
    result = ith_order_statistic(arr, 0, n - 1, i)
    print(f"The {i}th smallest element is: {result}")

