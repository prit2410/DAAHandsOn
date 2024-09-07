import time
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial


# Original function
def f_original(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x = x + 1
    return x


# Modified function
def f_modified(n):
    x = 1
    y = 1
    for i in range(n):
        for j in range(n):
            x = x + 1
            y = i + j
    return x


# Measure time for various n
ns = list(range(1, 10001, 500))  # Increasing to larger n for better illustration
times_original = []
times_modified = []

for n in ns:
    # Timing the original function
    start = time.time()
    f_original(n)
    end = time.time()
    times_original.append(end - start)

    # Timing the modified function
    start = time.time()
    f_modified(n)
    end = time.time()
    times_modified.append(end - start)

# Fitting a polynomial to the original function's timings
coeffs = np.polyfit(ns, times_original, 2)  # Quadratic fit
p = Polynomial(coeffs[::-1])  # Create Polynomial object for easy plotting

# Defining upper and lower bounds
upper_bound = lambda n: 1.2 * p(n)  # Adjust multipliers to get tight bounds
lower_bound = lambda n: 0.8 * p(n)  # Adjust multipliers to get tight bounds

# Plotting the time vs n for the original function
plt.figure(figsize=(18, 6))

# 1st Plot: Time vs n for the original function
plt.subplot(1, 3, 1)
plt.plot(ns, times_original, 'bo-', label='Original Function')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Time vs n for Original Function')
plt.grid(True)

# 2nd Plot: Time vs n with upper and lower bounds
plt.subplot(1, 3, 2)
plt.plot(ns, times_original, 'bo-', label='Time Taken')
plt.plot(ns, p(ns), 'r-', label='Fitted Curve')
plt.plot(ns, upper_bound(ns), 'g--', label='Upper Bound')
plt.plot(ns, lower_bound(ns), 'y--', label='Lower Bound')
plt.axvline(x=1800, color='grey', linestyle='--', label='n_0 = 1800')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Time vs n with Upper and Lower Bounds')
plt.legend()
plt.grid(True)

# 3rd Plot: Modified function with upper and lower bounds and n0
plt.subplot(1, 3, 3)
plt.plot(ns, times_modified, 'bo-', label='Modified Function')
plt.plot(ns, p(ns), 'r-', label='Fitted Curve')
plt.plot(ns, upper_bound(ns), 'g--', label='Upper Bound')
plt.plot(ns, lower_bound(ns), 'y--', label='Lower Bound')
plt.axvline(x=1800, color='grey', linestyle='--', label='n_0 = 1800')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Modified Function with Upper and Lower Bounds and n_0')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
