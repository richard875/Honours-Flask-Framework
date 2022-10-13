import time
import random

def cocktail_sort(sort_arr):
    a = sort_arr
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):
        # reset the swapped flag on entering the loop, because it might be true from a previous iteration.
        swapped = False
        
        # loop from left to right same as the bubble sort
        for i in range (start, end):
            if (a[i] > a[i+1]) :
                a[i], a[i+1]= a[i+1], a[i]
                swapped=True
        
        # if nothing moved, then array is sorted.
        if (swapped==False):
            break
        
        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False
        
        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end-1
        
        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end-1, start-1,-1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        
        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start+1
        
        return a

# Small: 4000000, Medium: 10000000, Large: 17000000
def cocktail_sort_test():
    time_variable = []
    len_num = [4000000, 10000000, 17000000]
    max_number = [4000000, 10000000, 17000000]

    for i in range(len(len_num)):
        list = []
        for i in range(len_num[i]):
            list.append(random.randint(0, max_number[i]))

        start = time.time()
        # -------------- Function start --------------
        result = cocktail_sort(list)
        # -------------- Function stop --------------
        end = time.time()

        time_variable.append(str(round(end - start, 3)))

    return time_variable

if __name__ == "__main__":
    print(cocktail_sort([4, 2, 3, 1]))