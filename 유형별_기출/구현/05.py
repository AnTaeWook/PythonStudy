import collections

size = int(input())
apple = int(input())

# 사과는 2로 시작점은 1로 초기화
arr = [[0]*size for _ in range(size)]
for _ in range(apple):
  temp = list(map(int, input().split()))
  arr[temp[0] - 1][temp[1] - 1] = 2
arr[0][0] = 1

change = int(input())
c_direction = []
for _ in range(change):
  c_direction.append(input().split())

# 방향 변경 리스트를 시간순으로 정렬
c_direction.sort(key = lambda x: int(x[0]))

# 방향에 따른 좌표 변경값
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 초기값 설정
direction = 0 
second = 0
x, y = 0, 0
idx = 0
queue = collections.deque([[0, 0]])
while True:
  # 방향을 바꿀 시간인지 확인
  if idx < len(c_direction):
    if second == int(c_direction[idx][0]):
      if c_direction[idx][1] == 'L':
        direction -= 1
      else:
        direction += 1
      idx += 1

  # 시간 증가
  second += 1

  # 지렁이 머리 이동
  x += dx[direction % len(dx)]
  y += dy[direction % len(dy)]

  # 게임이 끝나는지 검사
  if x < 0 or x >= size or y < 0 or y >= size or (arr[y][x] == 1):
    print(second)
    break
  
  # 사과를 먹지 않으면 꼬리를 움직임
  if arr[y][x] != 2:
    temp = queue.popleft()
    arr[temp[0]][temp[1]] = 0
  
  # 머리를 이동시키고 큐에 새 자리 삽입
  arr[y][x] = 1
  queue.append([y, x])


# 정확한 시뮬레이션이 중요한 문제
########################################################################