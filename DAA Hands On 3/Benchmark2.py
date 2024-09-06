import numpy as np
import matplotlib.pyplot as plt
import time

# Original function
def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x += 1

# Modified function
def f_modified(n):
    x = 1
    y = 1
    for i in range(n):
        for j in range(n):
            x += 1
            y = i + j

# Timing functions
def timed_f(n):
    start_time = time.time()
    f(n)
    return time.time() - start_time

def timed_f_modified(n):
    start_time = time.time()
    f_modified(n)
    return time.time() - start_time

# Timing and plotting for the original function
n_values = np.arange(1, 21)
times = np.array([timed_f(n) for n in n_values])

# Fit polynomial curve
p = np.polyfit(n_values, times, 2)
fitted_curve = np.polyval(p, n_values)

# Define Big-O and Big-Omega bounds
big_O = 0.5 * n_values**2
big_Omega = 0.1 * n_values**2

# Plot time vs. n for the original function
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, label='Measured Time', color='blue', marker='o', linestyle='-', markersize=3)
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Taken vs. n (Original Function)')
plt.grid(True)
plt.legend()
plt.show()

# Plot time vs. n with fitted curve and bounds
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, label='Measured Time', color='blue', marker='o', linestyle='-', markersize=3)
plt.plot(n_values, fitted_curve, label=f'Fitted Curve: {p[0]:.2e}n^2 + {p[1]:.2e}n + {p[2]:.2e}', color='red', linestyle='-', linewidth=2)
plt.plot(n_values, big_O, label='Upper Bound (Big-O)', color='green', linestyle='--', linewidth=1.5)
plt.plot(n_values, big_Omega, label='Lower Bound (Big-Omega)', color='orange', linestyle='--', linewidth=1.5)
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Taken, Fitted Curve, Upper Bound (O), and Lower Bound (Ω) (Original Function)')
plt.grid(True)
plt.legend()
plt.show()

# Timing and plotting for the modified function
times_modified = np.array([timed_f_modified(n) for n in n_values])

# Fit polynomial curve for modified function
p_modified = np.polyfit(n_values, times_modified, 2)
fitted_curve_modified = np.polyval(p_modified, n_values)

# Define Big-O and Big-Omega bounds (adjust if needed)
big_O_modified = 0.5 * n_values**2
big_Omega_modified = 0.1 * n_values**2

# Plot time vs. n for the modified function
plt.figure(figsize=(10, 6))
plt.plot(n_values, times_modified, label='Measured Time', color='blue', marker='o', linestyle='-', markersize=3)
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Taken vs. n (Modified Function)')
plt.grid(True)
plt.legend()
plt.show()

# Plot time vs. n with fitted curve and bounds for modified function
plt.figure(figsize=(10, 6))
plt.plot(n_values, times_modified, label='Measured Time', color='blue', marker='o', linestyle='-', markersize=3)
plt.plot(n_values, fitted_curve_modified, label=f'Fitted Curve: {p_modified[0]:.2e}n^2 + {p_modified[1]:.2e}n + {p_modified[2]:.2e}', color='red', linestyle='-', linewidth=2)
plt.plot(n_values, big_O_modified, label='Upper Bound (Big-O)', color='green', linestyle='--', linewidth=1.5)
plt.plot(n_values, big_Omega_modified, label='Lower Bound (Big-Omega)', color='orange', linestyle='--', linewidth=1.5)
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Taken, Fitted Curve, Upper Bound (O), and Lower Bound (Ω) (Modified Function)')
plt.grid(True)
plt.legend()
plt.show()

# Find and plot n_0 for the modified function
n_0 = 800  # Example value based on visual observation
plt.figure(figsize=(10, 6))
plt.plot(n_values, times_modified, label='Measured Time', color='blue', marker='o', linestyle='-', markersize=3)
plt.plot(n_values, fitted_curve_modified, label='Fitted Curve', color='red', linestyle='-', linewidth=2)
plt.plot(n_values, big_O_modified, label='Upper Bound (Big-O)', color='green', linestyle='--', linewidth=1.5)
plt.plot(n_values, big_Omega_modified, label='Lower Bound (Big-Omega)', color='orange', linestyle='--', linewidth=1.5)
plt.axvline(x=n_0, color='gray', linestyle='--', label=f'n_0 = {n_0}')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Taken, Fitted Curve, Upper Bound (O), Lower Bound (Ω) with n_0 (Modified Function)')
plt.grid(True)
plt.legend()
plt.show()
