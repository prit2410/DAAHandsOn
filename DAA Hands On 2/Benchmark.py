import random
import timeit
import platform
import psutil
import matplotlib.pyplot as plt

# Implementing the sorting algorithms
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Generate random array
def generate_random_array(size):
    return [random.uniform(0, 1000) for _ in range(size)]

# Benchmark sorting algorithms
def benchmark_sorting_algorithm(algorithm, input_sizes):
    execution_times = []
    for size in input_sizes:
        arr = generate_random_array(size)
        time_taken = timeit.timeit(lambda: algorithm(arr.copy()), number=1)
        execution_times.append((size, time_taken))
    return execution_times

# System information
def get_system_info():
    my_system = platform.uname()
    return (
        f"System: {my_system.system}\n"
        f"Node Name: {my_system.node}\n"
        f"Release: {my_system.release}\n"
        f"Machine: {my_system.machine}\n"
        f"Processor: {my_system.processor}\n"
        f"CPU: {psutil.cpu_count(logical=False)} physical cores, {psutil.cpu_count(logical=True)} logical cores\n"
        f"RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB"
    )

# Plotting the results
def plot_benchmark_results(algorithms, input_sizes):
    plt.figure(figsize=(10, 6))

    for algorithm in algorithms:
        times_for_algorithm = benchmark_sorting_algorithm(algorithm, input_sizes)
        sizes, times = zip(*times_for_algorithm)
        plt.plot(sizes, times, label=algorithm.__name__, marker='o')

    plt.xlabel('Input Size of Array')
    plt.ylabel('Time Taken for Execution (s)')
    plt.title('Benchmark for Insertion, Selection, and Bubble Sort Algorithms')
    plt.legend()

    # Display system information on the plot
    system_info = get_system_info()
    plt.text(0.02, 0.68, system_info, transform=plt.gca().transAxes, fontsize=9,
             bbox=dict(facecolor='white', alpha=0.8))

    plt.grid(True)
    plt.show()

# Input sizes for benchmarking
input_sizes = [5, 10, 20, 100, 1000, 2000, 5000, 10000]

# Sorting algorithms to be benchmarked
algorithms = [insertion_sort, selection_sort, bubble_sort]

# Plot the benchmark results
plot_benchmark_results(algorithms, input_sizes)
