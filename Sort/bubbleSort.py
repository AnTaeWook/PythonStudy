# 탐색 범위를 하나씩 줄여나감(가장 큰수는 가장 뒤로 밀리므로)
def bubble_sort(arr):
  for i in range(len(arr) - 1, 0 , -1):
    for j in range(i):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  

arr = [4, 3, 5, 1, 2]
bubble_sort(arr)
print(arr)

# 한 번도 swap이 일어나지 않았다면 정렬이 완료된 뜻으로
# 불필요한 반복문을 탈출함으로써 최적화가 가능

def bubble_sort_opt(arr):
  isSwap = False
  for i in range(len(arr) - 1, 0 , -1):
    for j in range(i):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        isSwap = True
    if not isSwap:
      break

arr2 = [4, 3, 5, 1, 2]
bubble_sort_opt(arr)
print(arr)