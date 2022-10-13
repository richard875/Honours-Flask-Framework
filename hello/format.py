def format(rest_result):
    test_functions = ["Bitonic sort", "Brick Sort", "Bubble Sort", "Bucket Sort", "Cocktail Sort", "Comb Sort", "Gnome Sort", "Heap Sort", "Insertion Sort", "Merge Sort", "Pancake Sort", "Pigeonhole Sort", "Quick Sort", "Radix Sort", "Selection Sort", "Shell Sort", "Smooth Sort", "Strand Sort"]
    string_builder = ""

    for key in rest_result:
        string_builder += f"<h2>{key}:</h2>"

        for i in range(len(rest_result[key])):
            string_builder += f"<h4 style='margin: 0;'>{test_functions[i]}: {rest_result[key][i]}s</h4>"

    return string_builder