import random
import timeit
import platform
import psutil
import matplotlib.pyplot as plt

# Define sorting algorithms
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

# System information
my_system = platform.uname()
system_info = (
    f"System: {my_system.system}\n"
    f"Node Name: {my_system.node}\n"
    f"Release: {my_system.release}\n"
    f"Machine: {my_system.machine}\n"
    f"Processor: {my_system.processor}\n"
    f"CPU: {psutil.cpu_count()} cores"
)
ram_info = f"RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB"

# Benchmark sorting algorithms
def benchmark_sorting_algorithm(algorithm, input_sizes):
    execution_times = []
    for size in input_sizes:
        arr = generate_random_array(size)
        time_taken = timeit.timeit(lambda: algorithm(arr.copy()), number=1)
        execution_times.append((size, time_taken))
    return execution_times

# Generate random array
def generate_random_array(size):
    return [random.uniform(0, 1000) for _ in range(size)]

# Input sizes for benchmarking
input_sizes = [5, 10, 20, 100, 1000, 2000, 5000, 10000]

# Collecting data for all algorithms
algorithms = [insertion_sort, selection_sort, bubble_sort]
data = {}
for algorithm in algorithms:
    times_for_algorithm = benchmark_sorting_algorithm(algorithm, input_sizes)
    sizes, times = zip(*times_for_algorithm)
    data[algorithm.__name__] = times

# Plotting
plt.figure(figsize=(12, 8), facecolor='black')

ax = plt.gca()
ax.set_facecolor('black')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

line_styles = ['-', '--', '-.']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

for i, (algorithm, times) in enumerate(data.items()):
    plt.plot(input_sizes, times, label=algorithm, linestyle=line_styles[i], color=colors[i], marker='D')

plt.xlabel('Input Size of Array', color='white')
plt.ylabel('Time Taken for Execution (s)', color='white')
plt.title('Benchmark for Insertion, Selection, and Bubble Sort Algorithms', color='white', fontsize=14)
plt.legend(facecolor='black', edgecolor='white', fontsize=10)

# Add system information as text annotation
plt.text(0.02, 0.5, system_info + '\n' + ram_info, transform=plt.gca().transAxes, fontsize=10,
         verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

plt.grid(True, color='#666666')
plt.show()
