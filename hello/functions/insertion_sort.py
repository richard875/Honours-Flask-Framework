''' BIG O
Best case - O(n)
Medium case - O(n^2)
Worst case - O(n^2)
'''

import time
import random

def insertion_sort(arr):
    p = 1
    sort_list = arr
    n = len(sort_list)
    while (p < n):
        temp = sort_list[p]
        j = p
        while (j > 0 and temp < sort_list[j - 1]):
            sort_list[j] = sort_list[j - 1]
            j -= 1
        sort_list[j] = temp
        p += 1

    return sort_list

def insertion_sort_test(len_num, max_number):
    list = []
    for i in range(len_num):
        list.append(random.randint(0, max_number))

    start = time.time()
    # -------------- Function start --------------
    result = insertion_sort(list)
    # -------------- Function stop --------------
    end = time.time()

    return str(round(end - start, 3))

if __name__ == "__main__":
    print(insertion_sort([4, 2, 3, 1]))