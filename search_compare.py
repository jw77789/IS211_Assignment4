import time
import random

def sequential_search(lst, target):
    start_time = time.perf_counter()
    for item in lst:
        if item == target:
            return True, time.perf_counter() - start_time
    return False, time.perf_counter() - start_time

def ordered_sequential_search(lst, target):
    start_time = time.perf_counter()
    for item in lst:
        if item == target:
            return True, time.perf_counter() - start_time
        elif item > target:
            break
    return False, time.perf_counter() - start_time

def binary_search_iterative(lst, target):
    start_time = time.perf_counter()
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return True, time.perf_counter() - start_time
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False, time.perf_counter() - start_time

def binary_search_recursive(lst, target, left, right, start_time):
    if left > right:
        return False, time.perf_counter() - start_time
    mid = (left + right) // 2
    if lst[mid] == target:
        return True, time.perf_counter() - start_time
    elif lst[mid] < target:
        return binary_search_recursive(lst, target, mid + 1, right, start_time)
    else:
        return binary_search_recursive(lst, target, left, mid - 1, start_time)

def run_search_tests():
    sizes = [500, 1000, 5000]
    target = 99999999
    
    for size in sizes:
        seq_time = ord_seq_time = bin_iter_time = bin_rec_time = 0
        
        for _ in range(100):
            lst = [random.randint(1, 100000) for _ in range(size)]
            sorted_lst = sorted(lst)
            
            _, t = sequential_search(lst, target)
            seq_time += t
            
            _, t = ordered_sequential_search(sorted_lst, target)
            ord_seq_time += t
            
            _, t = binary_search_iterative(sorted_lst, target)
            bin_iter_time += t
            
            _, t = binary_search_recursive(sorted_lst, target, 0, len(sorted_lst) - 1, time.perf_counter())
            bin_rec_time += t
        
        print(f"Sequential Search took {seq_time / 100:10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {ord_seq_time / 100:10.7f} seconds to run, on average")
        print(f"Binary Search (Iterative) took {bin_iter_time / 100:10.7f} seconds to run, on average")
        print(f"Binary Search (Recursive) took {bin_rec_time / 100:10.7f} seconds to run, on average")

def insertion_sort(lst):
    start_time = time.perf_counter()
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return time.perf_counter() - start_time

def shell_sort(lst):
    start_time = time.perf_counter()
    gap = len(lst) // 2
    while gap > 0:
        for i in range(gap, len(lst)):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return time.perf_counter() - start_time
