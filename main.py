import random
import time

def generate_random_array(size, max_val):
    return [random.randint(0, max_val) for _ in range(size)]

def shell(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def radix(arr, base=10):
    if len(arr) == 0:
        return arr

    # Determina maximul din array
    max_val = max(arr)

    # Determina numarul de cifre necesare
    num_digits = 0
    while max_val > 0:
        num_digits += 1
        max_val //= base

    # Sorteaza array-ul pe fiecare cifra
    for i in range(num_digits):
        buckets = [[] for j in range(base)]
        for j in arr:
            digit = j // (base**i) % base
            buckets[digit].append(j)
        arr = [item for bucket in buckets for item in bucket]
    
    return arr

def merge(arr) :
    if len(arr) > 1:
        mid = len(arr) // 2
        
        left = arr[:mid]
        right = arr[mid:]

        merge(left)
        merge(right)

        i=j=k=0
        

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                
                arr[k] = left[i]
                i += 1
            else:

                arr[k] = right[j]
                j += 1

            k += 1



        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def test_sorting_algorithms(arr):
    radix_start = time.time()
    sorted_arr = radix(arr)
    radix_end = time.time()
    print("Radix sort:", radix_end - radix_start, "seconds")

    merge_start = time.time()
    sorted_arr = merge(arr)
    merge_end = time.time()
    print("Merge sort:", merge_end - merge_start, "seconds")

    shell_start = time.time()
    sorted_arr = shell(arr)
    shell_end = time.time()
    print("Shell sort:", shell_end - shell_start, "seconds")

    quick_start = time.time()
    sorted_arr = quick_sort(arr)
    quick_end = time.time()
    print("Quick sort:", quick_end - quick_start, "seconds")


size = 10000
max_val = 1000000
arr = generate_random_array(size, max_val)

test_sorting_algorithms(arr)


def bucket(arr, bucket_size=5):
    if len(arr) == 0:
        return arr

  
    min_value, max_value = min(arr), max(arr)

   
    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    0
    for i in range(len(arr)):
        bucket_index = (arr[i] - min_value) // bucket_size
        buckets[bucket_index].append(arr[i])


    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])

    
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr


