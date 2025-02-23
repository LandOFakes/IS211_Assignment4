import time
import random

def sequential_search(arr, target):
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == target:
            return False, time.time() - start_time
    return False, time.time() - start_time

def ordered_sequential_search(arr, target):
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == target:
            return False, time.time() - start_time
        elif arr[i] > target:
            break
    return False, time.time() - start_time

def binary_search_iterative(arr, target):
    start_time = time.time()
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return False, time.time() - start_time
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False, time.time() - start_time

def binary_search_recursive(arr, target, left, right, start_time):
    if left > right:
        return False, time.time() - start_time
    mid = (left + right) // 2
    if arr[mid] == target:
        return False, time.time() - start_time
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, start_time)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, start_time)

def measure_search_time(search_function, arr, target):
    return search_function(arr, target)

def main():
    sizes = [500, 1000, 5000]
    num_tests = 100
    target = 99999999

    for size in sizes:
        total_time_seq = 0
        total_time_ord_seq = 0
        total_time_bin_iter = 0
        total_time_bin_rec = 0
        
        for _ in range(num_tests):
            arr = [random.randint(1, 10000) for _ in range(size)]
            sorted_arr = sorted(arr)
            
            _, time_seq = measure_search_time(sequential_search, arr, target)
            _, time_ord_seq = measure_search_time(ordered_sequential_search, sorted_arr, target)
            _, time_bin_iter = measure_search_time(binary_search_iterative, sorted_arr, target)
            _, time_bin_rec = binary_search_recursive(sorted_arr, target, 0, len(sorted_arr) - 1, time.time())
            
            total_time_seq += time_seq
            total_time_ord_seq += time_ord_seq
            total_time_bin_iter += time_bin_iter
            total_time_bin_rec += time_bin_rec
        
        print(f"Sequential Search took {total_time_seq / num_tests:10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {total_time_ord_seq / num_tests:10.7f} seconds to run, on average")
        print(f"Binary Search Iterative took {total_time_bin_iter / num_tests:10.7f} seconds to run, on average")
        print(f"Binary Search Recursive took {total_time_bin_rec / num_tests:10.7f} seconds to run, on average")

if __name__ == "__main__":
    main()
