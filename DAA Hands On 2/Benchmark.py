import random
import timeit
import numpy as npy
import matplotlib.pyplot as pltlb
import platform
import psutil

def bubble_sort_implementation(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

def selection_sort_implementation(a):
    for i in range(len(a)):
        small = i
        for j in range(i + 1, len(a)):
            if a[j] < a[small]:
                small = j
        a[i], a[small] = a[small], a[i]

def insertion_sort_implementation(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

def generate_random_array(size):
    return [random.uniform(0, 1000) for _ in range(size)]  # Generating float values between 0 and 1000

def benchmark_sorting_algorithm(algorithm, input_sizes):
    execution_times = []

    for size in input_sizes:
        arr = generate_random_array(size)
        time_taken = timeit.timeit(lambda: algorithm(arr.copy()), number=1)
        execution_times.append((size, time_taken))

    return execution_times

input_sizes = [5, 10, 20, 100, 1000, 2000]
algorithms = [insertion_sort_implementation, selection_sort_implementation, bubble_sort_implementation]
pltlb.figure(figsize=(10, 6))

for algorithm in algorithms:
    times_for_algorithm = benchmark_sorting_algorithm(algorithm, input_sizes)
    sizes, times = zip(*times_for_algorithm)
    pltlb.plot(sizes, times, label=algorithm.__name__, marker='o')

pltlb.xlabel('Input Size of Array')
pltlb.ylabel('Time Taken for Execution (s)')
pltlb.title('Benchmark for Insertion, Selection, and Bubble Sort Algorithms')
pltlb.legend()

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

# Display system information as text in a box on the plot
pltlb.text(0.95, 0.05, system_info, transform=pltlb.gca().transAxes, fontsize=10,
         verticalalignment='bottom', horizontalalignment='right',
         bbox=dict(facecolor='white', alpha=0.5))

pltlb.grid(True)
pltlb.show()
