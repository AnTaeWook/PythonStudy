# dfs, bfs - 2번
from collections import deque

# bfs정의
def bfs(y, x):

  # 큐 생성 및 탐색 완료 표시
  queue = deque([[y, x]])
  graph[y][x] = 1

  # 사방 탐색
  dy = [0, -1, 0, 1]
  dx = [-1, 0, 1, 0]

  # bfs탐색 시작
  while queue:
    # 원소 꺼내기
    np = queue.popleft()
    y = np[0]
    x = np[1]

    # 주변 노드 검사
    for i in range(len(dx)):
      ny = y + dy[i]
      nx = x + dx[i]

      # 인덱스 범위 초과 및 시작점인지 검사
      if ny < 0 or ny >= n or nx < 0 or nx >= m or (ny == 0 and nx == 0):
        continue
      if graph[ny][nx] == 1:
        if ny == n - 1 and nx == m - 1:
          print(graph[y][x] + 1)
          return
        queue.append([ny, nx])
        graph[ny][nx] = graph[y][x] + 1


# 입력값 받기
n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

bfs(0, 0)
