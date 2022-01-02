# 쉽지만 효율성이 떨어짐
def selection_sort(arr):
  for i in range(len(arr) - 1):
    min_idx = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [3, 4, 1, 5, 2]
selection_sort(arr)
print(arr)