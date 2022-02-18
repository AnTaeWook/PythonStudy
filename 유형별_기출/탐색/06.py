from itertools import combinations
import copy

# 입력 받기
n = int(input())
hallway = []
for _ in range(n):
  h = []
  temp = input().split()
  for t in temp:
    if t == 'X':
      h.append(0)
    elif t == 'S':
      h.append(1)
    else:
      h.append(2)
  hallway.append(h)

# 선생님 위치 리스트
teacher = []
empty = []
for i in range(n):
  for j in range(n):
    if hallway[i][j] == 2:
      teacher.append([i, j])

# 빈 공간 리스트
empty = []
for i in range(n):
  for j in range(n):
    if hallway[i][j] == 0:
      empty.append([i, j])

# 장애물 설치 조합
objects = list(combinations(empty, 3))

# 선생님 감시 알고리즘
def watch(hallway, x, y):
  global isPossible

  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]
  
  for i in range(len(dx)):
    tx = x
    ty = y
    while True:
      tx += dx[i]
      ty += dy[i]
      if tx < 0 or tx >= n or ty < 0 or ty >= n:
        break
      if hallway[tx][ty] == 1:
        isPossible = False
        return
      if hallway[tx][ty] == 3:
        break

for case in objects:
  isPossible = True
  hallway_copy = copy.deepcopy(hallway)
  # 장애물 설치
  for position in case:
    hallway_copy[position[0]][position[1]] = 3
  # 감시
  for t in teacher:
    watch(hallway_copy, t[0], t[1])
  if isPossible:
    break

# 감시를 피할 수 있다면
if isPossible:
  print('YES')
else:
  print('NO')
  
# 정답은 watch함수를 구현할 때 방향을 각각 타이핑 하였음
# 복도를 초기화 할 때 글자를 숫자로 바꾸는 과정을 거쳤는데, 불필요한 과정이였음
