INF = int(1e9)

# 입력 받기
n, m = map(int, input().split())

# 그래프 초기화
graph = [[1e9]*(n + 1) for _ in range(n + 1)]

# 자기 자신까지의 거리는 0
for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i == j:
      graph[i][j] = 0

# 간선 정보 입력받아 대입
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

# 플로이드 워셜 알고리즘 실행
for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 소개팅, 회사 입력받기
x, k = map(int, input().split())

# 정답 출력
if graph[1][k] + graph[k][x] >= INF:
  print(-1)
else:
  print(graph[1][k] + graph[k][x]) 