import time
import random

def insertion_sort(arr):
    start_time = time.perf_counter()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return time.perf_counter() - start_time


def shell_sort(arr):
    start_time = time.perf_counter()
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return time.perf_counter() - start_time


def python_sort(arr):
    start_time = time.perf_counter()
    arr.sort()
    return time.perf_counter() - start_time

def main():
    sizes = [500, 1000, 5000]
    num_tests = 100

    for size in sizes:
        total_time_insertion = 0
        total_time_shell = 0
        total_time_python = 0
        
        for _ in range(num_tests):
            arr = [random.randint(1, 10000) for _ in range(size)]
            total_time_insertion += insertion_sort(arr[:])
            total_time_shell += shell_sort(arr[:])
            total_time_python += python_sort(arr[:])
        
        print(f"List Size: {size}")
        print(f"Insertion Sort took {total_time_insertion / num_tests:.7f} seconds on average")
        print(f"Shell Sort took {total_time_shell / num_tests:.7f} seconds on average")
        print(f"Python Sort took {total_time_python / num_tests:.7f} seconds on average")
        print("-" * 50)

if __name__ == "__main__":
    main()


