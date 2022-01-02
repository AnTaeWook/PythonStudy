# 2개의 원소비교 부터 시작해서 하나씩 늘리며 정렬
def insertion_sort(arr):
  for end in range(1, len(arr)):
    for i in range(end, 0, -1):
      if arr[i - 1] > arr[i]:
        arr[i - 1], arr[i] = arr[i], arr[i - 1]

arr = [5, 1, 4, 2, 3]
insertion_sort(arr)
print(arr)

# 두번째 반복문에서 작은값이 더 없으면 불필요한 비교를 하지
# 않음으로써 최적화가 가능
def insertion_sort_opt(arr):
  for end in range(1, len(arr)):
    i = end
    while i > 0 and arr[i - 1] > arr[i]:
      arr[i - 1], arr[i] = arr[i], arr[i - 1]
      i -= 1

arr2 = [5, 3, 2, 1, 4]
insertion_sort_opt(arr)
print(arr)
