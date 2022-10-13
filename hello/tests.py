import os
import time
import random

from functions.bitonic_sort import bitonic_sort_test
from functions.brick_sort import brick_sort_test
from functions.bubble_sort import bubble_sort_test
from functions.bucket_sort import bucket_sort_test
from functions.cocktail_sort import cocktail_sort_test
from functions.comb_sort import comb_sort_test
from functions.gnome_sort import gnome_sort_test
from functions.heap_sort import heap_sort_test
from functions.insertion_sort import insertion_sort_test
from functions.merge_sort import merge_sort_test
from functions.pancake_sort import pancake_sort_test
from functions.pigeonhole_sort import pigeonhole_sort_test
from functions.quick_sort import quick_sort_test
from functions.radix_sort import radix_sort_test
from functions.selection_sort import selection_sort_test
from functions.shell_sort import shell_sort_test
from functions.smooth_sort import smooth_sort_test
from functions.strand_sort import strand_sort_test


def main():
    times = [10, 100, 1000]
    max_number = [10, 100, 1000]
    tests = {}

    for i in range(len(times)):
        time_variable = []
        print('                                        ')
        print('Test with {} times and max number {}'.format(times[i], max_number[i]))
        print('----------------------------------------')

        bitonic_sort = bitonic_sort_test(times[i], max_number[i])
        brick_sort = brick_sort_test(times[i], max_number[i])
        bubble_sort = bubble_sort_test(times[i], max_number[i])
        bucket_sort = bucket_sort_test(times[i], max_number[i])
        cocktail_sort = cocktail_sort_test(times[i], max_number[i])
        comb_sort = comb_sort_test(times[i], max_number[i])
        gnome_sort = gnome_sort_test(times[i], max_number[i])
        heap_sort = heap_sort_test(times[i], max_number[i])
        insertion_sort = insertion_sort_test(times[i], max_number[i])
        merge_sort = merge_sort_test(times[i], max_number[i])
        pancake_sort = merge_sort_test(times[i], max_number[i])
        pigeonhole_sort = pancake_sort_test(times[i], max_number[i])
        quick_sort = quick_sort_test(times[i], max_number[i])
        radix_sort = radix_sort_test(times[i], max_number[i])
        selection_sort = selection_sort_test(times[i], max_number[i])
        shell_sort = shell_sort_test(times[i], max_number[i])
        smooth_sort = smooth_sort_test(times[i], max_number[i])
        strand_sort = strand_sort_test(times[i], max_number[i])

        print('Bitonic sort: {}s'.format(bitonic_sort))
        print('Brick Sort: {}s'.format(brick_sort))
        print('Bubble Sort: {}s'.format(bubble_sort))
        print('Bucket Sort: {}s'.format(bucket_sort))
        print('Cocktail Sort: {}s'.format(cocktail_sort))
        print('Comb Sort: {}s'.format(comb_sort))
        print('Gnome Sort: {}s'.format(gnome_sort))
        print('Heap Sort: {}s'.format(heap_sort))
        print('Insertion Sort: {}s'.format(insertion_sort))
        print('Merge Sort: {}s'.format(merge_sort))
        print('Pancake Sort: {}s'.format(pancake_sort))
        print('Pigeonhole Sort: {}s'.format(pigeonhole_sort))
        print('Quick Sort: {}s'.format(quick_sort))
        print('Radix Sort: {}s'.format(radix_sort))
        print('Selection Sort: {}s'.format(selection_sort))
        print('Shell Sort: {}s'.format(shell_sort))
        print('Smooth Sort: {}s'.format(smooth_sort))
        print('Strand Sort: {}s'.format(strand_sort))

        time_variable.append(bitonic_sort)
        time_variable.append(brick_sort)
        time_variable.append(bubble_sort)
        time_variable.append(bucket_sort)
        time_variable.append(cocktail_sort)
        time_variable.append(comb_sort)
        time_variable.append(gnome_sort)
        time_variable.append(heap_sort)
        time_variable.append(insertion_sort)
        time_variable.append(merge_sort)
        time_variable.append(pancake_sort)
        time_variable.append(pigeonhole_sort)
        time_variable.append(quick_sort)
        time_variable.append(radix_sort)
        time_variable.append(selection_sort)
        time_variable.append(shell_sort)
        time_variable.append(smooth_sort)
        time_variable.append(strand_sort)

        tests[f"Test with {times[i]} times and max number {max_number[i]}"] = time_variable
    
    return tests

if __name__ == "__main__":
    main()