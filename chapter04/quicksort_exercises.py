def sum(arr):
  if len(arr) == 0:
    return 0
  return arr[0] + sum(arr[1:])

def count_len(arr):
  if(arr):
    return 1 + count_len(arr[1:])
  return 0

def maximum_number(arr):
  if(len(arr) == 2 ):
    return arr[0] if arr[0] > arr[1] else arr[1]  
  return arr[0] if arr[0]  > maximum_number(arr[1:]) else maximum_number(arr[1:]) 

print(sum([0,1,2,3,4]))
print(count_len([1,2,3,4]))
print(maximum_number([1,2,10]))

def quicksort(array):
  if(len(array) < 2):
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot ]
    greater = [i for i in array[1:] if i > pivot] 

  return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))