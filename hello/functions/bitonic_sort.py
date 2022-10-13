import time
import random

def compare_swap(a, i, j, d):
    if (d == 1 and a[i] > a[j]) or (d == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]
  
def merge(a, l, cnt, d):
    if cnt > 1:
        k = int(cnt / 2)
        for i in range(l, l + k):
            compare_swap(a, i, i + k, d)
        merge(a, l, k, d)
        merge(a, l + k, k, d)
 
def bitonic_sort_algorithm(sort_arr, l, cnt, d):
    a = sort_arr

    if cnt > 1:
        k = int(cnt / 2)
        bitonic_sort_algorithm(a, l, k, 1)
        bitonic_sort_algorithm(a, l + k, k, 0)
        merge(a, l, cnt, d)
    
    return a
    
def bitonic_sort(a):
    return bitonic_sort_algorithm(a, 0, len(a), 1)

def bitonic_sort_test(len_num, max_number):
    list = []
    for i in range(len_num):
        list.append(random.randint(0, max_number))

    start = time.time()
    # -------------- Function start --------------
    result = bitonic_sort(list)
    # -------------- Function stop --------------
    end = time.time()

    return str(round(end - start, 3))

if __name__ == "__main__":
    print(bitonic_sort([4, 2, 3, 1]))