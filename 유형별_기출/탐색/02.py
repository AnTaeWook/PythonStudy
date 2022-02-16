from collections import deque
from itertools import combinations
import copy

# bfs로 완전 탐색
def bfs(graph, x, y):
  # 가로, 세로 길이 제한 확인
  n = len(graph)
  m = len(graph[0])
  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  # 연구소를 순회하며 탐색할 것이기 때문에 바이러스=3 으로 표시
  queue = deque([[x, y]])
  graph[y][x] = 3
  while queue:
    q = queue.popleft()
    for i in range(len(dx)):
      x, y = q[0], q[1]
      nx = x + dx[i]
      ny = y + dy[i]
      # 인덱스 범위를 초과하는지 검사
      if nx < 0 or nx >= m or ny < 0 or ny >= n:
        continue
      
      if graph[ny][nx] == 0:
        graph[ny][nx] = 3
        queue.append([nx, ny])

# 입력값 대입
n, m = map(int, input().split())
center = []
for _ in range(n):
  center.append(list(map(int, input().split())))

# 벽을 세울 수 있는 공간
space = []
for y in range(n):
  for x in range(m):
    if center[y][x] == 0:
      space.append([x, y])

# 벽을 세울 수 있는 모든 경우
walls = list(combinations(space, 3))

# 정답
answer = 0

for wall in walls:
  center_copy = copy.deepcopy(center)
  center_copy[wall[0][1]][wall[0][0]] = 1
  center_copy[wall[1][1]][wall[1][0]] = 1
  center_copy[wall[2][1]][wall[2][0]] = 1
  
  for y in range(n):
    for x in range(m):
      if center_copy[y][x] == 2:
        bfs(center_copy, x, y)

  # 안전 영역 수
  safety = 0

  for y in range(n):
    for x in range(m):
      if center_copy[y][x] == 0:
        safety += 1
  
  if safety > answer:
    answer = safety

print(answer)