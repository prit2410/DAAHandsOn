import random
import time
from openpyxl import Workbook

def selection_sort(arr):
    start_time = time.time_ns()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    end_time = time.time_ns()
    return end_time - start_time

def insertion_sort(arr):
    start_time = time.time_ns()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end_time = time.time_ns()
    return end_time - start_time

def bubble_sort(arr):
    start_time = time.time_ns()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    end_time = time.time_ns()
    return end_time - start_time

def main():
    n = 1000  # Number of different array sizes to test
    random.seed(0)  # Seed for reproducibility

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Sorting Performance Results"

    # Create header row
    sheet.append(["Array Size", "Selection Sort (ns)", "Insertion Sort (ns)", "Bubble Sort (ns)"])

    for i in range(1, n + 1):
        size = i * 5
        arr = [random.randint(1, 10000) for _ in range(size)]

        # Clone the array for fair comparison
        arr_selection = arr.copy()
        arr_insertion = arr.copy()
        arr_bubble = arr.copy()

        # Measure time taken by each sorting algorithm
        selection_sort_time = selection_sort(arr_selection)
        insertion_sort_time = insertion_sort(arr_insertion)
        bubble_sort_time = bubble_sort(arr_bubble)

        # Write the results to the Excel file
        sheet.append([size, selection_sort_time, insertion_sort_time, bubble_sort_time])

        # Display progress
        print(f"Array Size: {size} | Progress: {i * 100 // n}%")

    # Save the workbook to a file
    workbook.save("SortingPerformanceResults.xlsx")
    print("Successfully written data to the Excel sheet.")

if __name__ == "__main__":
    main()
