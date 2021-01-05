"""
-----------------------------
Author: Matthew Woolley
Email: matt.wool@live.com.au
-----------------------------

Script comparing algorithm runtime over various length lists
"""

import matplotlib.pyplot as plt
import random
import time


from list_search_functions.list_search_functions import (
    binary_search,
    exponential_search,
    fibonacci_search,
    interpolation_search,
)

SEARCH_FUNCS = [
    binary_search,
    exponential_search,
    fibonacci_search,
    interpolation_search,
]

MAX_POWER = 8
SEED = 100

random.seed(SEED)

array_lengths = [10 ** power for power in range(MAX_POWER + 1)]
search_func_runtimes = [[] for _ in range(len(SEARCH_FUNCS))]
for array_len in array_lengths:
    array = [random.randint(-array_len // 2, array_len // 2) for _ in range(array_len)]
    array.sort()
    element = random.choice(array)
    for func, func_runtimes in zip(SEARCH_FUNCS, search_func_runtimes):
        start_time = time.time_ns()
        func(array, element)
        func_runtimes.append(time.time_ns() - start_time)

for func, func_runtimes in zip(SEARCH_FUNCS, search_func_runtimes):
    plt.plot(array_lengths, func_runtimes, label=func.__name__, marker="o")

plt.title("Runtime comparison of search algorithms")
plt.xlabel("Array length")
plt.ylabel("Runtime (ns)")
plt.xscale("log")
plt.ylim(bottom=0.0)
plt.legend()
plt.show()
