import random
import time

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

sizes = [1000, 5000, 10000, 50000]

for size in sizes:

    data = [random.randint(1,100000) for _ in range(size)]

    start = time.perf_counter()
    bubble_sort(data)
    bubble_time = time.perf_counter()-start

    start = time.perf_counter()
    sorted(data)
    quick_time = time.perf_counter()-start

    print("Dataset size:", size)
    print("Bubble Sort:", bubble_time)
    print("Quick Sort:", quick_time)
