import time
import random

def brick_sort(sort_arr):
    arr = sort_arr
    n = len(arr)
    isSorted = 0
    while isSorted == 0: 
          isSorted = 1
          temp = 0
          for i in range(1, n-1, 2): 
            if arr[i] > arr[i+1]: 
                    arr[i], arr[i+1] = arr[i+1], arr[i] 
                    isSorted = 0
            for i in range(0, n-1, 2): 
                if arr[i] > arr[i+1]: 
                    arr[i], arr[i+1] = arr[i+1], arr[i] 
                    isSorted = 0
      
    return arr

# Small: 600, Medium: 800, Large: 1000
def brick_sort_test(len_num, max_number):
    list = []
    for i in range(len_num):
        list.append(random.randint(0, max_number))

    start = time.time()
    # -------------- Function start --------------
    result = brick_sort(list)
    # -------------- Function stop --------------
    end = time.time()

    return str(round(end - start, 3))

if __name__ == "__main__":
    print(brick_sort([4, 2, 3, 1]))