# bisect 모듈 사용
import bisect

# 입력 받기
n, x = map(int, input().split())
arr = list(map(int, input().split()))

# 일단 x가 있는지 확인
arr_set = set(arr)
if x in arr_set:
  # bisect로 좌 인덱스와 우 인덱스 구하기
  left = bisect.bisect_left(arr, x)
  right = bisect.bisect_right(arr, x)
  print(right - left)
# x가 없는 경우
else:
  print(-1)
  
# bisect 사용 익숙해지기(중요)
# 이진 탐색을 구현하여 풀 수 있어야함