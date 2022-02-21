# 입력 받기
n = int(input())
arr = list(map(int, input().split()))

# 이진 탐색
start = 0
end = n - 1
isExist = False
while start <= end:
  mid = (start + end)//2
  # 인덱스보다 값이 크면 좌측 탐색
  if arr[mid] > mid:
    end = mid - 1
  # 인덱스보다 값이 작으면 우측 탐색
  elif arr[mid] < mid:
    start = mid + 1
  else:
    print(mid)
    isExist = True
    break

# 고정값이 존재하지 않으면
if not isExist:
  print(-1)

# 정답에선 반복문 대신 while문으로 이진탐색을 구현하였음