n = int(input())
have = list(map(int, input().split()))
m = int(input())
need = list(map(int, input().split()))

have.sort()

# 이진 탐색
def binary_search(array, target, start, end):

  if start > end:
    return False
  mid = (start + end) // 2

  if array[mid] == target:
    return True
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  else:
    return binary_search(array, target, mid + 1, end)

 # 부품이 존재하는지 검사
for i in need:
  if binary_search(have, i, 0, n - 1):
    print('yes')
  else:
    print('no')


# 이진 탐색을 이용하여 풀었지만
# 계수 정렬의 개념을 이용하여 문제를 풀 수도 있고
# 집합(set)자료형을 이용하면 더 빠르고 간단하게 풀 수 있다(중요)