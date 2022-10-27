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

# Small: 20000, Medium: 30000, Large: 35000
def strand_sort_test():
    time_variable = []
    len_num = [20000, 30000, 35000]
    max_number = [20000, 30000, 35000]

    for i in range(len(len_num)):
      list = []
      for j in range(len_num[i]):
          list.append(random.randint(0, max_number[i]))

      start = time.time()
      # -------------- Function start --------------
      result = strand_sort(list)
      # -------------- Function stop --------------
      end = time.time()

      time_variable.append(str(round(end - start, 3)))

    return time_variable

if __name__ == "__main__":
  print(strand_sort([4, 2, 3, 1]))