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

def python_sort(lst):
    start_time = time.perf_counter()
    lst.sort()
    return time.perf_counter() - start_time

def run_sort_tests():
    sizes = [500, 1000, 5000]
    
    for size in sizes:
        ins_time = shell_time = py_time = 0
        
        for _ in range(100):
            lst = [random.randint(1, 100000) for _ in range(size)]
            
            t = insertion_sort(lst[:])
            ins_time += t
            
            t = shell_sort(lst[:])
            shell_time += t
            
            t = python_sort(lst[:])
            py_time += t
        
        print(f"Insertion Sort took {ins_time / 100:10.7f} seconds to run, on average")
        print(f"Shell Sort took {shell_time / 100:10.7f} seconds to run, on average")
        print(f"Python Sort took {py_time / 100:10.7f} seconds to run, on average")

if __name__ == "__main__":
    print("Running search comparisons...")
    run_search_tests()
    print("\nRunning sorting comparisons...")
    run_sort_tests()
        avg_time = total_time / 100
        print(f"Insertion sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
