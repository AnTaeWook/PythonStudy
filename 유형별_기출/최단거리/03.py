INF = int(1e9)
import heapq

# 입력 받기
n = int(input())
answer = []
# 테스트 케이스 만큼 입력받으며 정답리스트에 추가
for _ in range(n):
  m = int(input())
  # 지도 정보 입력받기
  graph = []
  for _ in range(m):
    graph.append(list(map(int, input().split())))

  # 다익스트라 알고리즘
  visited = [[False]*m for _ in range(m)]
  distance = [[INF]*m for _ in range(m)]
  q = []
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  heapq.heappush(q, [graph[0][0], 0, 0])
  while q:
    d, x, y = heapq.heappop(q)
    if visited[x][y]:
      continue
    visited[x][y] = True
    distance[x][y] = d
    for i in range(len(dx)):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= m or ny < 0 or ny >= m:
        continue
      heapq.heappush(q, [d + graph[nx][ny], nx, ny])
  # 꼭지점까지의 최단거리를 추가
  answer.append(distance[m - 1][m - 1])

# 정답 출력
for a in answer:
  print(a)