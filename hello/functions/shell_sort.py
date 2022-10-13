''' BIG O
Best case - O(n)
Medium case - O((n log(n)) ^ 2)
Worst case - O((n log(n)) ^ 2)
'''

import time
import random

def shell_sort(sort_arr):
    array = sort_arr
    n = len(array)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2
    
    return array

# Small: 190000, Medium: 400000, Large: 700000
def shell_sort_test():
    time_variable = []
    len_num = [190000, 400000, 700000]
    max_number = [190000, 400000, 700000]

    for i in range(len(len_num)):
        list = []
        for j in range(len_num[i]):
            list.append(random.randint(0, max_number[i]))

        start = time.time()
        # -------------- Function start --------------
        result = shell_sort(list)
        # -------------- Function stop --------------
        end = time.time()

        time_variable.append(str(round(end - start, 3)))

    return time_variable

if __name__ == "__main__":
    print(shell_sort([4, 2, 3, 1]))