import time
import random

def comb_sort(sort_arr):
    num = sort_arr
    gap = len(num)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(num) - gap):
            j = i+gap
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]
                swaps = True
                
    return num

# Small: 250000, Medium: 550000, Large: 850000
def comb_sort_test():
    time_variable = []
    len_num = [250000, 550000, 850000]
    max_number = [250000, 550000, 850000]

    for i in range(len(len_num)):
        list = []
        for j in range(len_num[i]):
            list.append(random.randint(0, max_number[i]))

        start = time.time()
        # -------------- Function start --------------
        result = comb_sort(list)
        # -------------- Function stop --------------
        end = time.time()

        time_variable.append(str(round(end - start, 3)))

    return time_variable

if __name__ == "__main__":
    print(comb_sort([4, 2, 3, 1]))