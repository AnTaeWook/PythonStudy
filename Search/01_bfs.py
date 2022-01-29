# dfs, bfs - 1번
# bfs풀이

from collections import deque

# BFS함수 정의
def bfs(graph, position):
  # 큐 생성 및 시작지점 완료표시
  queue = deque([position])
  graph[position[0]][position[1]] = 1

  # 4방향 주변 좌표 배열
  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  # bfs탐색 시작
  while queue:
    p = queue.popleft()
    # 특정지점 4방향 주변 탐색
    for i in range(len(dx)):
      np = (p[0] + dy[i], p[1] + dx[i])
      # 인덱스 범위 검사
      if np[0] < 0 or np[0] >= n or np[1] < 0 or np[1] >= m:
        continue
      # 큐에 푸쉬 및 완료표시
      if graph[np[0]][np[1]] == 0:
        queue.append(np)
        graph[np[0]][np[1]] = 1

n, m = map(int, input().split())

# 입력받기
arr = []
for _ in range(n):
  arr.append(list(map(int, input())))

# 배열을 순회하며 bfs수행 및 카운트
count = 0
for i in range(n):
  for j in range(m):
    if arr[i][j] == 0:
      bfs(arr, (i, j))
      count += 1

print(count)