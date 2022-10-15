import time
import random

def gnome_sort(arr):
    n = len(arr)
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index = index - 1

    return arr

# Small: 4000, Medium: 6500, Large: 9000
def gnome_sort_test():
    time_variable = []
    len_num = [4000, 6500, 9000]
    max_number = [4000, 6500, 9000]

    for i in range(len(len_num)):
        list = []
        for j in range(len_num[i]):
            list.append(random.randint(0, max_number[i]))

        start = time.time()
        # -------------- Function start --------------
        result = gnome_sort(list)
        # -------------- Function stop --------------
        end = time.time()

        time_variable.append(str(round(end - start, 3)))

    return time_variable

if __name__ == "__main__":
    print(gnome_sort([4, 2, 3, 1]))