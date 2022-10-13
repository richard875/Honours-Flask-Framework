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
    tests = {}
    print('----------------------------------------')

    start = time.time()
    bitonic_sort = bitonic_sort_test()
    brick_sort = brick_sort_test()
    bubble_sort = bubble_sort_test()
    bucket_sort = bucket_sort_test()
    cocktail_sort = cocktail_sort_test()
    comb_sort = comb_sort_test()
    gnome_sort = gnome_sort_test()
    heap_sort = heap_sort_test()
    insertion_sort = insertion_sort_test()
    merge_sort = merge_sort_test()
    pancake_sort = pancake_sort_test()
    pigeonhole_sort = pigeonhole_sort_test()
    quick_sort = quick_sort_test()
    radix_sort = radix_sort_test()
    selection_sort = selection_sort_test()
    shell_sort = shell_sort_test()
    smooth_sort = smooth_sort_test()
    strand_sort = strand_sort_test()
    end = time.time()

    total_time = str(round(end - start, 3))

    print('Bitonic sort: {}'.format(bitonic_sort))
    print('Brick Sort: {}'.format(brick_sort))
    print('Bubble Sort: {}'.format(bubble_sort))
    print('Bucket Sort: {}'.format(bucket_sort))
    print('Cocktail Sort: {}'.format(cocktail_sort))
    print('Comb Sort: {}'.format(comb_sort))
    print('Gnome Sort: {}'.format(gnome_sort))
    print('Heap Sort: {}'.format(heap_sort))
    print('Insertion Sort: {}'.format(insertion_sort))
    print('Merge Sort: {}'.format(merge_sort))
    print('Pancake Sort: {}'.format(pancake_sort))
    print('Pigeonhole Sort: {}'.format(pigeonhole_sort))
    print('Quick Sort: {}'.format(quick_sort))
    print('Radix Sort: {}'.format(radix_sort))
    print('Selection Sort: {}'.format(selection_sort))
    print('Shell Sort: {}'.format(shell_sort))
    print('Smooth Sort: {}'.format(smooth_sort))
    print('Strand Sort: {}'.format(strand_sort))
    print("Total time: {}".format(total_time))

    tests['Bitonic sort'] = bitonic_sort
    tests['Brick Sort'] = brick_sort
    tests['Bubble Sort'] = bubble_sort
    tests['Bucket Sort'] = bucket_sort
    tests['Cocktail Sort'] = cocktail_sort
    tests['Comb Sort'] = comb_sort
    tests['Gnome Sort'] = gnome_sort
    tests['Heap Sort'] = heap_sort
    tests['Insertion Sort'] = insertion_sort
    tests['Merge Sort'] = merge_sort
    tests['Pancake Sort'] = pancake_sort
    tests['Pigeonhole Sort'] = pigeonhole_sort
    tests['Quick Sort'] = quick_sort
    tests['Radix Sort'] = radix_sort
    tests['Selection Sort'] = selection_sort
    tests['Shell Sort'] = shell_sort
    tests['Smooth Sort'] = smooth_sort
    tests['Strand Sort'] = strand_sort

    print(tests)
    return tests, total_time

if __name__ == "__main__":
    main()