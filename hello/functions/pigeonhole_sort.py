import time
import random

def pigeonhole_sort(items):
    biggest = max(items)
    smallest = min(items)
    size = biggest - smallest + 1
    holes = [0] * size

    for item in items:
        holes[item - smallest] += 1

    i = 0
    for j in range(size):
        while holes[j] > 0:
            holes[j] -= 1
            items[i] = j + smallest
            i += 1
    
    return items

# Small: 4000000, Medium: 11000000, Large: 20000000
def pigeonhole_sort_test():
    time_variable = []
    len_num = [4000000, 11000000, 11000000]
    max_number = [4000000, 11000000, 11000000]

    for i in range(len(len_num)):
        list = []
        for i in range(len_num[i]):
            list.append(random.randint(0, max_number[i]))

        start = time.time()
        # -------------- Function start --------------
        result = pigeonhole_sort(list)
        # -------------- Function stop --------------
        end = time.time()

        time_variable.append(str(round(end - start, 3)))

    return time_variable

if __name__ == "__main__":
    print(pigeonhole_sort([4, 2, 3, 1]))