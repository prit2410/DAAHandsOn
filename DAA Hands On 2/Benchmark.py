import platform
import psutil
import random
import time
import matplotlib.pyplot as plt

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def benchmark_sorting_algorithms():
    sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]  # Varying input sizes
    insertion_times = []
    selection_times = []
    bubble_times = []

    for size in sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]

        start_time = time.time()
        insertion_sort(arr.copy())
        insertion_times.append(time.time() - start_time)

        start_time = time.time()
        selection_sort(arr.copy())
        selection_times.append(time.time() - start_time)

        start_time = time.time()
        bubble_sort(arr.copy())
        bubble_times.append(time.time() - start_time)

    # Plotting the results
    plt.figure(figsize=(12, 8))
    plt.plot(sizes, insertion_times, label="Insertion Sort", marker='o')
    plt.plot(sizes, selection_times, label="Selection Sort", marker='o')
    plt.plot(sizes, bubble_times, label="Bubble Sort", marker='o')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Benchmarking Sorting Algorithms")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")  # Use log scale for better visualization
    plt.yscale("log")

    # Get system information
    my_system = platform.uname()
    system_info = (
        f"System: {my_system.system}\n"
        f"Node Name: {my_system.node}\n"
        f"Release: {my_system.release}\n"
        f"Machine: {my_system.machine}\n"
        f"Processor: {my_system.processor}\n"
        f"CPU: {psutil.cpu_count()} cores\n"
        f"RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB"
    )

    # Display system information as text in a box
    plt.figtext(0.99, 0.01, system_info, horizontalalignment='right', fontsize=10,
                bbox=dict(facecolor='lightgray', alpha=0.5))

    plt.show()

# Run the benchmark
benchmark_sorting_algorithms()
