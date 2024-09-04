import time
import numpy as np
import matplotlib.pyplot as plt

# Define the function to be analyzed
def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x = x + 1
    return x

# Generate n values and time the function for each n
n_values = np.arange(1, 1001)  # n from 1 to 1000
times = []

# Time the function for each n
for n in n_values:
    start_time = time.time()
    f(n)
    end_time = time.time()
    times.append(end_time - start_time)

# Fit a polynomial to the timing data (2nd degree polynomial since T(n) ~ n^2)
p = np.polyfit(n_values, times, 2)
fitted_curve = np.polyval(p, n_values)

# Define upper and lower bounds based on the fitted curve
upper_bound = 1.1 * fitted_curve  # Example: 10% higher as upper bound (Big-O)
lower_bound = 0.9 * fitted_curve  # Example: 10% lower as lower bound (Big-Omega)

# Define Big-Omega (fitted curve as lower bound) and Big-O (upper bound)
big_Omega = lower_bound
big_O = upper_bound

# Graph 1: Time Taken vs. n
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, label='Measured Time', color='blue', marker='o', linestyle='-', markersize=3)
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Taken vs. n')
plt.grid(True)
plt.legend()
plt.show()

# Graph 2: Time Taken, Fitted Curve, Upper Bound (Big-O), and Lower Bound (Big-Omega)
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, label='Measured Time', color='blue', marker='o', linestyle='-', markersize=3)
plt.plot(n_values, fitted_curve, label=f'Fitted Curve: {p[0]:.2e}n^2 + {p[1]:.2e}n + {p[2]:.2e}', color='red', linestyle='-', linewidth=2)
plt.plot(n_values, big_O, label='Upper Bound (Big-O)', color='green', linestyle='--', linewidth=1.5)
plt.plot(n_values, big_Omega, label='Lower Bound (Big-Omega)', color='orange', linestyle='--', linewidth=1.5)
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Taken, Fitted Curve, Upper Bound (O), and Lower Bound (Ω)')
plt.grid(True)
plt.legend()
plt.show()

# Graph 3: Time Taken, Fitted Curve, Upper Bound (Big-O), Lower Bound (Big-Omega) with n_0
n_0 = 800  # Example value based on visual observation
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, label='Measured Time', color='blue', marker='o', linestyle='-', markersize=3)
plt.plot(n_values, fitted_curve, label='Fitted Curve', color='red', linestyle='-', linewidth=2)
plt.plot(n_values, big_O, label='Upper Bound (Big-O)', color='green', linestyle='--', linewidth=1.5)
plt.plot(n_values, big_Omega, label='Lower Bound (Big-Omega)', color='orange', linestyle='--', linewidth=1.5)
plt.axvline(x=n_0, color='gray', linestyle='--', label=f'n_0 = {n_0}')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Taken, Fitted Curve, Upper Bound (O), Lower Bound (Ω) with n_0')
plt.grid(True)
plt.legend()
plt.show()
