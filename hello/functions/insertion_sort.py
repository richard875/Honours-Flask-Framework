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

# Small: 6000, Medium: 10000, Large: 14000
def insertion_sort_test():
    time_variable = []
    len_num = [6000, 10000, 14000]
    max_number = [6000, 10000, 14000]

    for i in range(len(len_num)):
        list = []
        for i in range(len_num[i]):
            list.append(random.randint(0, max_number[i]))

        start = time.time()
        # -------------- Function start --------------
        result = insertion_sort(list)
        # -------------- Function stop --------------
        end = time.time()

        time_variable.append(str(round(end - start, 3)))

    return time_variable

if __name__ == "__main__":
    print(insertion_sort([4, 2, 3, 1]))