import time
import random

def strand_sort(inp):
  output = strand(inp)
  while len(inp):
    output = merge(output, strand(inp))
  return output
   
   
def strand(inp):
  element, sub = 0, [inp.pop(0)]
  while element < len(inp):
    if inp[element] > sub[-1]:
      sub.append(inp.pop(element))
    else:
      element += 1
  return sub
  
def merge(a, b):
  output = []
  while len(a) and len(b):
    if a[0] < b[0]:
      output.append(a.pop(0))
    else:
      output.append(b.pop(0))
  output += a
  output += b
  return output

def strand_sort_test(len_num, max_number):
    list = []
    for i in range(len_num):
        list.append(random.randint(0, max_number))

    start = time.time()
    # -------------- Function start --------------
    result = strand_sort(list)
    # -------------- Function stop --------------
    end = time.time()

    return str(round(end - start, 3))

if __name__ == "__main__":
  print(strand_sort([4, 2, 3, 1]))