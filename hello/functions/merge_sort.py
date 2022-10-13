''' BIG O
Best case - O(n log(n))
Medium case - O(n log(n))
Worst case - O(n log(n))
'''

import time
import random

def merge_sort(arr):
    obj = arr

    if len(obj) > 1:
        mid = int(len(obj) / 2)
        left = obj[:mid]
        right = obj[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                obj[k] = left[i]
                i += 1
            else:
                obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            obj[k] = right[j]
            j += 1
            k += 1

    return obj

# Small: 300000, Medium: 700000, Large: 1400000
def merge_sort_test(len_num, max_number):
    list = []
    for i in range(len_num):
        list.append(random.randint(0, max_number))

    start = time.time()
    # -------------- Function start --------------
    result = merge_sort(list)
    # -------------- Function stop --------------
    end = time.time()

    return str(round(end - start, 3))

if __name__ == "__main__":
    print(merge_sort([4, 2, 3, 1]))