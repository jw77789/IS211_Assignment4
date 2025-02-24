import time
import random

def get_me_random_list(size):
    """Generate a list of random positive integers."""
    return [random.randint(1, 10000) for _ in range(size)]

def sequential_search(lst, target):
    """Performs a sequential search and records time taken."""
    start_time = time.perf_counter()
    for item in lst:
        if item == target:
            return True, time.perf_counter() - start_time
    return False, time.perf_counter() - start_time

def ordered_sequential_search(lst, target):
    """Performs a sequential search on a sorted list and records time taken."""
    start_time = time.perf_counter()
    for item in lst:
        if item == target:
            return True, time.perf_counter() - start_time
        elif item > target:
            break
    return False, time.perf_counter() - start_time

def binary_search_iterative(lst, target):
    """Performs an iterative binary search and records time taken."""
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

def binary_search_recursive(lst, target, left, right, start_time=None):
    """Performs a recursive binary search and records time taken."""
    if start_time is None:
        start_time = time.perf_counter()
    
    if left > right:
        return False, time.perf_counter() - start_time
    
    mid = (left + right) // 2
    if lst[mid] == target:
        return True, time.perf_counter() - start_time
    elif lst[mid] < target:
        return binary_search_recursive(lst, target, mid + 1, right, start_time)
    else:
        return binary_search_recursive(lst, target, left, mid - 1, start_time)

if __name__ == "__main__":
    """Main entry point"""
    the_size = 500
    total_time = 0

    for i in range(100):
        mylist = get_me_random_list(the_size)
       
        mylist = sorted(mylist)

        start = time.time()
        check = binary_search_iterative(mylist, 99999999)  
        time_spent = time.time() - start
        total_time += time_spent

    avg_time = total_time / 100
    print(f"Binary Search Iterative took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
