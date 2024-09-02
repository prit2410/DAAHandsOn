import time
import random
import platform
import psutil
import matplotlib.pyplot as plt


# System Information
def get_system_info():
    system_info = {
        "PC Name": platform.node(),
        "Processor": platform.processor(),
        "RAM": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
        "CPU Count": psutil.cpu_count(logical=True),
        "Python Version": platform.python_version()
    }
    return system_info


# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # Corrected this line
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Benchmarking
def benchmark_sorting_algorithms():
    input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
    algorithms = {
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Bubble Sort": bubble_sort
    }

    results = {alg: [] for alg in algorithms}

    for size in input_sizes:
        arr = random.sample(range(size * 10), size)  # Generate a random array of the given size
        for name, algorithm in algorithms.items():
            start_time = time.time()
            algorithm(arr.copy())  # Run the algorithm
            elapsed_time = time.time() - start_time
            results[name].append(elapsed_time)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(input_sizes, times, label=name, marker='o')

    plt.title("Sorting Algorithms Runtime Benchmark")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.yscale("log")
    plt.legend()
    plt.grid(True)
    plt.show()


# Main execution
if __name__ == "__main__":
    # Display system information
    system_info = get_system_info()
    print("System Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")
    print("\nRunning benchmarks...\n")

    # Run the benchmark
    benchmark_sorting_algorithms()
