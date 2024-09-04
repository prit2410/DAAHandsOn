import time
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# Define the function to be analyzed
def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x = x + 1
    return x

# Generate n values and time the function for each n
n_values = np.arange(1, 101)  # n from 1 to 100
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

# Plot "Time" vs "n"
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, label='Measured Time', color='blue', marker='o', linestyle='-')
plt.plot(n_values, fitted_curve, label=f'Fitted Curve: {p[0]:.2e}n^2 + {p[1]:.2e}n + {p[2]:.2e}', color='red', linestyle='-')

# Upper and Lower bounds (just example bounds to illustrate, adjust as needed)
upper_bound = 1.1 * fitted_curve
lower_bound = 0.9 * fitted_curve

plt.plot(n_values, upper_bound, label='Upper Bound', color='green', linestyle='--')
plt.plot(n_values, lower_bound, label='Lower Bound', color='orange', linestyle='--')

plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time vs n with Fitted Curve and Bounds')
plt.grid(True)
plt.legend()
plt.show()
