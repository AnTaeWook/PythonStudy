# quick sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quicksort(array, start, end):
  if start >= end:
    return
  
  pivot = start
  left = start + 1
  right = end

  while left <= right:
    while left <= end and array[left] <= array[pivot]:
      left += 1
    while right > start and array[right] >= array[pivot]:
      right -= 1
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[right], array[left] = array[left], array[right]

  quicksort(array, start, right - 1)
  quicksort(array, right + 1, end)

# 파이썬 스러운 퀵정렬(시간 복잡도는 손해)
def pythontic(array):
  if len(array) <= 1:
    return array

  pivot = array[0]
  tail = array[1:]

  left = [x for x in tail if x <= pivot]
  right = [x for x in tail if x > pivot]
  
  return pythontic(left) + [pivot] + pythontic(right)


print(pythontic(array))
quicksort(array, 0, len(array) - 1)
print(array)