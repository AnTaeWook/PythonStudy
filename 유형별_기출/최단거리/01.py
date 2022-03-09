INF = int(1e9)

# 도시, 버스 수 입력받기
n = int(input())
m = int(input())

# 버스 정보 입력받아서 그래프 완성하기
graph = [[1e9]*(n + 1) for _ in range(n + 1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  if c < graph[a][b]: 
    graph[a][b] = c
  
# 자기 자신에게 가는 거리는 0
for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i == j:
      graph[i][j] = 0

# 플로이드워셜 알고리즘
for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if graph[i][k] + graph[k][j] < graph[i][j]:
        graph[i][j] = graph[i][k] + graph[k][j]

# 구해진 노드별 최단거리 출력
for i in range(1, n + 1):
  for j in range(1, n + 1):
    if graph[i][j] >= INF:
      print(0, end=' ')
    else:
      print(graph[i][j], end=' ')
  print()