import time
import random

def flip(arr, i): 
    start = 0
    while start < i: 
        temp = arr[start] 
        arr[start] = arr[i] 
        arr[i] = temp 
        start += 1
        i -= 1

def findMax(arr, n): 
    mi = 0
    for i in range(0,n): 
        if arr[i] > arr[mi]: 
            mi = i 
    return mi 

def pancake_sort(sort_arr):
    arr = sort_arr
    curr_size = len(arr)
    while curr_size > 1: 
        # Find index of the maximum element in arr[0..curr_size-1] 
        mi = findMax(arr, curr_size) 
        # Move the maximum element to end of current array  if it's not already at the end 
        if mi != curr_size-1: 
            # To move at the end, first move maximum number to beginning  
            flip(arr, mi)
            # Now move the maximum number to end by reversing current array 
            flip(arr, curr_size-1) 
        curr_size -= 1
    
    return arr

# Small: 4500, Medium: 7000, Large: 10000
def pancake_sort_test(len_num, max_number):
    list = []
    for i in range(len_num):
        list.append(random.randint(0, max_number))

    start = time.time()
    # -------------- Function start --------------
    result = pancake_sort(list)
    # -------------- Function stop --------------
    end = time.time()

    return str(round(end - start, 3))

if __name__ == "__main__":
    print(pancake_sort([4, 2, 3, 1]))