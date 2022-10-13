''' BIG O
Best case - O(n^2)
Medium case - O(n^2)
Worst case - O(n^2)
'''

import time
import random

def selection_sort(sort_arr):
    arr = sort_arr
    i = 0
    n = len(arr)
    while(i<n):
        j=i+1
        min = i
        while(j<n):
            if(arr[j] < arr[min]):
                min = j 
            j+=1

        arr[i], arr[min] = arr[min], arr[i]
        i+=1
    
    return arr

# Small: 6000, Medium: 9500, Large: 14000
def selection_sort_test():
    time_variable = []
    len_num = [6000, 9500, 14000]
    max_number = [6000, 9500, 14000]

    for i in range(len(len_num)):
        list = []
        for j in range(len_num[i]):
            list.append(random.randint(0, max_number[i]))

        start = time.time()
        # -------------- Function start --------------
        result = selection_sort(list)
        # -------------- Function stop --------------
        end = time.time()

        time_variable.append(str(round(end - start, 3)))

    return time_variable

if __name__ == "__main__":
    print(selection_sort([4, 2, 3, 1]))