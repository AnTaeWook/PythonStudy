import sys

# 입력 받기
n, c = map(int, sys.stdin.readline().rstrip().split())
home = []
for _ in range(n):
  home.append(int(sys.stdin.readline().rstrip()))

# 집 위치 정렬
home.sort()

# 설치해야 할 공유기 개수가 두 대인 경우
if c == 2:
  print(home[-1] - home[0])
else:
  # 이진 탐색하며 설치 가능한 집 개수 카운팅 및 비교
  start = 1
  end = home[-1] - home[0]
  result = 0
  while start <= end:
    gap = (start + end)//2
    value = home[0]
    count = 1
    for h in home:
      if h >= value + gap:
        value = h
        count += 1
    # 설치 가능한 집 개수가 부족하면 설치 거리 줄이기
    if count < c:
      end = gap - 1
    # 충분하면 저장 후 설치 거리 늘리기
    else:
      result = gap
      start = gap + 1

  print(result)
  
# 이진 탐색을 사용할 때 무엇을 찾아야 하는지 정확히 인지하기